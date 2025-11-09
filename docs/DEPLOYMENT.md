# Deployment Guide

## Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured
- Docker installed
- Python 3.9+
- Twilio Account

## Local Development Setup

### 1. Environment Configuration

Create `.env` file in `src/API/`:

```bash
RUN_INSTANCE=local
TABLE_NAME=CarBon_Data
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
NUMBER=your_twilio_phone_number
ALLOWED_URLS=http://localhost:3000,http://localhost:8080
```

### 2. Install Dependencies

```bash
cd src/API
poetry install
poetry shell
```

### 3. Run Locally

```bash
uvicorn app.index:app --reload --host 0.0.0.0 --port 8080
```

Access at: `http://localhost:8080/docs`

## AWS Lambda Deployment

### Step 1: Create DynamoDB Tables

```bash
# CarBon_Data table
aws dynamodb create-table \
  --table-name CarBon_Data \
  --attribute-definitions \
    AttributeName=device_id,AttributeType=S \
    AttributeName=timestamp,AttributeType=N \
  --key-schema \
    AttributeName=device_id,KeyType=HASH \
    AttributeName=timestamp,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST

# user_table
aws dynamodb create-table \
  --table-name user_table \
  --attribute-definitions \
    AttributeName=id,AttributeType=S \
  --key-schema \
    AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

### Step 2: Create Secrets in AWS Secrets Manager

```bash
aws secretsmanager create-secret \
  --name Car-Bon-Secrets \
  --secret-string '{
    "TABLE_NAME":"CarBon_Data",
    "ACCOUNT_SID":"your_twilio_sid",
    "AUTH_TOKEN":"your_twilio_token",
    "NUMBER":"your_twilio_number",
    "ALLOWED_URLS":"https://yourdomain.com"
  }'
```

### Step 3: Create ECR Repository

```bash
aws ecr create-repository --repository-name carbon-api
```

### Step 4: Build and Push Docker Image

```bash
# Get ECR login
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin \
  123456789.dkr.ecr.us-east-1.amazonaws.com

# Build image
docker build -t carbon-api:latest -f src/API/Dockerfile .

# Tag image
docker tag carbon-api:latest \
  123456789.dkr.ecr.us-east-1.amazonaws.com/carbon-api:latest

# Push image
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/carbon-api:latest
```

### Step 5: Create IAM Role

```bash
# Create trust policy
cat > trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "lambda.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}
EOF

# Create role
aws iam create-role \
  --role-name carbon-lambda-role \
  --assume-role-policy-document file://trust-policy.json

# Attach policies
aws iam attach-role-policy \
  --role-name carbon-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam attach-role-policy \
  --role-name carbon-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess

aws iam attach-role-policy \
  --role-name carbon-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/SecretsManagerReadWrite
```

### Step 6: Create Lambda Function

```bash
aws lambda create-function \
  --function-name carbon-api \
  --package-type Image \
  --code ImageUri=123456789.dkr.ecr.us-east-1.amazonaws.com/carbon-api:latest \
  --role arn:aws:iam::123456789:role/carbon-lambda-role \
  --timeout 30 \
  --memory-size 512
```

### Step 7: Create Function URL

```bash
aws lambda create-function-url-config \
  --function-name carbon-api \
  --auth-type NONE \
  --cors '{
    "AllowOrigins": ["*"],
    "AllowMethods": ["GET","POST","PUT","DELETE"],
    "AllowHeaders": ["*"],
    "MaxAge": 300
  }'
```

### Step 8: Add Resource Policy

```bash
aws lambda add-permission \
  --function-name carbon-api \
  --statement-id FunctionURLAllowPublicAccess \
  --action lambda:InvokeFunctionUrl \
  --principal "*" \
  --function-url-auth-type NONE
```

## CloudFormation Deployment

Use the provided template:

```bash
aws cloudformation deploy \
  --template-file infra/IaC/yaml/car-bon_infra.yml \
  --stack-name carbon-stack \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    LambdaFunction00carbon00eSP9PCodeS3BucketOneOfDYW9Z=your-bucket \
    LambdaFunction00carbon00eSP9PCodeS3KeyOneOfnaRpU=carbon-api.zip
```

## Monitoring Setup

### CloudWatch Alarms

```bash
# Lambda errors
aws cloudwatch put-metric-alarm \
  --alarm-name carbon-api-errors \
  --alarm-description "Alert on Lambda errors" \
  --metric-name Errors \
  --namespace AWS/Lambda \
  --statistic Sum \
  --period 300 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold

# DynamoDB throttling
aws cloudwatch put-metric-alarm \
  --alarm-name carbon-dynamodb-throttles \
  --metric-name UserErrors \
  --namespace AWS/DynamoDB \
  --statistic Sum \
  --period 60 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold
```

## Update Deployment

```bash
# Build new image
docker build -t carbon-api:latest -f src/API/Dockerfile .

# Push to ECR
docker tag carbon-api:latest \
  123456789.dkr.ecr.us-east-1.amazonaws.com/carbon-api:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/carbon-api:latest

# Update Lambda
aws lambda update-function-code \
  --function-name carbon-api \
  --image-uri 123456789.dkr.ecr.us-east-1.amazonaws.com/carbon-api:latest
```

## Rollback

```bash
# List versions
aws lambda list-versions-by-function --function-name carbon-api

# Rollback to previous version
aws lambda update-alias \
  --function-name carbon-api \
  --name prod \
  --function-version <previous-version>
```

## Testing Deployment

```bash
# Get Function URL
FUNCTION_URL=$(aws lambda get-function-url-config \
  --function-name carbon-api \
  --query FunctionUrl \
  --output text)

# Test endpoint
curl "$FUNCTION_URL/Dynamo/tables"
```

## Cost Optimization

- Use DynamoDB On-Demand billing for variable loads
- Enable Lambda provisioned concurrency for consistent latency
- Set up CloudWatch log retention policies
- Use S3 lifecycle policies for backups

## Security Checklist

- [ ] Enable encryption at rest for DynamoDB
- [ ] Use Secrets Manager for credentials
- [ ] Enable CloudTrail logging
- [ ] Configure VPC for Lambda (optional)
- [ ] Implement API Gateway with API keys
- [ ] Enable WAF for DDoS protection
- [ ] Regular security audits

---

*Last Updated: 2025-11-09*
