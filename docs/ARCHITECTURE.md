# System Architecture Documentation

## Table of Contents

- [Overview](#overview)
- [Architecture Patterns](#architecture-patterns)
- [System Components](#system-components)
- [Data Flow](#data-flow)
- [Infrastructure Architecture](#infrastructure-architecture)
- [Security Architecture](#security-architecture)
- [Scalability & Performance](#scalability--performance)

## Overview

Car-Bon implements a **serverless microservices architecture** with the following key characteristics:

- **Event-Driven**: Asynchronous communication between components
- **Loosely Coupled**: Independent service deployment and scaling
- **Cloud-Native**: Leverages AWS managed services
- **Edge Computing**: IoT devices perform initial data processing
- **Real-time Processing**: Immediate alerting for critical conditions

## Architecture Patterns

### 1. Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  PRESENTATION TIER                       │
│  ┌────────────────┐              ┌──────────────────┐  │
│  │  React Web UI  │              │  Dash Dashboard  │  │
│  │  (Port 5173)   │              │  (Port 8080)     │  │
│  └────────────────┘              └──────────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    APPLICATION TIER                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │            FastAPI Application Layer              │  │
│  │                                                    │  │
│  │  ┌─────────────┐  ┌──────────────┐              │  │
│  │  │   Routers   │  │  Middleware  │              │  │
│  │  │  - DynamoDB │  │  - CORS      │              │  │
│  │  │  - User     │  │  - Auth      │              │  │
│  │  │  - Notify   │  │  - Logging   │              │  │
│  │  │  - Graph    │  │              │              │  │
│  │  └─────────────┘  └──────────────┘              │  │
│  │                                                    │  │
│  │  ┌───────────────────────────────────────────┐  │  │
│  │  │         Service Layer                      │  │  │
│  │  │  - DynamoService                           │  │  │
│  │  │  - UserService                             │  │  │
│  │  │  - TwilioService                           │  │  │
│  │  │  - GraphService                            │  │  │
│  │  │  - SecretManagerService                    │  │  │
│  │  └───────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                      DATA TIER                           │
│  ┌──────────────────┐  ┌────────────────────────────┐  │
│  │   DynamoDB       │  │    External Services       │  │
│  │  - CarBon_Data   │  │  - Twilio API              │  │
│  │  - user_table    │  │  - AWS Secrets Manager     │  │
│  └──────────────────┘  │  - CloudWatch Logs         │  │
│                        └────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### 2. Microservices Architecture

Each service is independently deployable and scalable:

#### Service Breakdown

**DynamoDB Service** (`dynamo.py`)
- Responsibility: All database operations
- Operations: CRUD operations, querying, batch processing
- Tables: CarBon_Data, user_table

**User Service** (`user_service.py`)
- Responsibility: User management
- Operations: User registration, profile management, contact retrieval
- Data Model: User entity with ULID-based IDs

**Notification Service** (`twilio_service.py`)
- Responsibility: Alert and communication
- Operations: SMS, Voice calls, Emergency notifications
- Integration: Twilio REST API

**Graph Service** (`graph_service.py`)
- Responsibility: Data visualization
- Operations: Chart generation, time-series analysis
- Output: SVG/Base64 encoded graphs

**Secret Manager Service** (`secret_manager.py`)
- Responsibility: Credential management
- Operations: Retrieve secrets from AWS Secrets Manager
- Security: Encrypted credential storage

## System Components

### 1. IoT Edge Layer

```
┌─────────────────────────────────┐
│         ESP32 Device            │
│                                 │
│  ┌──────────────────────────┐  │
│  │   CO Sensor (MQ-7)       │  │
│  │   - Analog Reading       │  │
│  │   - Calibration Logic    │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │   WiFi Module            │  │
│  │   - HTTP Client          │  │
│  │   - SSL/TLS Support      │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │   Local Processing       │  │
│  │   - Data Aggregation     │  │
│  │   - Threshold Check      │  │
│  └──────────────────────────┘  │
└─────────────────────────────────┘
```

### 2. API Gateway Layer

**AWS Lambda + FastAPI**
- Runtime: Python 3.10
- Handler: Mangum (ASGI adapter)
- Trigger: Function URL / API Gateway
- Memory: 512MB - 1024MB
- Timeout: 30 seconds

**Key Features:**
- Automatic scaling
- Pay-per-request pricing
- Built-in monitoring
- Environment isolation

### 3. Data Storage Layer

#### DynamoDB Tables

**CarBon_Data Table**
```
Partition Key: device_id (String)
Sort Key: timestamp (Number)

Attributes:
- device_id: String (e.g., "ESP32")
- timestamp: Number (Unix timestamp)
- CO: String (Carbon monoxide reading)
- temperature: Number (Optional)
- humidity: Number (Optional)

Indexes:
- GSI: timestamp-index (for time-based queries)

Capacity: On-Demand (auto-scaling)
```

**user_table Table**
```
Partition Key: id (String - ULID)

Attributes:
- id: String (ULID format)
- name: String
- registered_device_id: String
- personal_contact: String (E.164 format)
- secondary_contacts: List[String]
- emergency_contacts: Map

Capacity: On-Demand with auto-scaling
```

## Data Flow

### 1. Sensor Data Collection Flow

```
┌─────────┐     ┌─────────┐     ┌──────────┐     ┌──────────┐
│ ESP32   │────▶│  WiFi   │────▶│  Lambda  │────▶│ DynamoDB │
│ Device  │     │ Network │     │ Function │     │          │
└─────────┘     └─────────┘     └──────────┘     └──────────┘
     │                                │
     │                                │
     ▼                                ▼
  CO Sensor                    POST /Dynamo/item
  Reading                      {device_id, Temp, 
                                Hum, CO}
```

**Step-by-Step:**

1. **Sensor Reading** (ESP32)
   - MQ-7 sensor measures CO concentration
   - Analog-to-Digital conversion
   - Local calibration applied

2. **Data Transmission** (ESP32)
   - HTTP POST to Lambda endpoint
   - Payload: `{device_id, Temp, Hum, CO}`
   - SSL/TLS encryption

3. **API Processing** (Lambda)
   - Request validation
   - PPM calculation
   - Timestamp generation

4. **Data Storage** (DynamoDB)
   - Write to CarBon_Data table
   - Automatic indexing
   - CloudWatch logging

### 2. Alert Notification Flow

```
┌──────────┐     ┌─────────┐     ┌─────────┐     ┌──────────┐
│ DynamoDB │────▶│ Lambda  │────▶│ Twilio  │────▶│   User   │
│ (Query)  │     │Function │     │   API   │     │  Phone   │
└──────────┘     └─────────┘     └─────────┘     └──────────┘
     │                │
     │                │
     ▼                ▼
  High CO         Threshold
  Detected        Exceeded?
```

**Trigger Conditions:**
- CO level > threshold (e.g., 50 PPM)
- Rapid CO increase detected
- Manual alert triggered by user

**Notification Types:**
1. **SMS Alert**
   - Immediate text message
   - CO level and timestamp
   - Action recommendations

2. **Voice Call**
   - Automated voice message
   - TwiML voice response
   - Emergency instructions

### 3. Data Visualization Flow

```
┌─────────┐     ┌─────────┐     ┌──────────┐     ┌─────────┐
│   User  │────▶│ FastAPI │────▶│ DynamoDB │────▶│ Graph   │
│   UI    │     │ Router  │     │  Query   │     │ Service │
└─────────┘     └─────────┘     └──────────┘     └─────────┘
     ▲                                                  │
     │                                                  │
     └──────────────────────────────────────────────────┘
              Base64 Encoded SVG Graph
```

**Query Parameters:**
- `start_date`: ISO 8601 datetime
- `end_date`: ISO 8601 datetime
- `graph_type`: Line | Bar
- `device`: Device ID

**Processing:**
1. Parse date range
2. Query DynamoDB with time range
3. Calculate CO PPM values
4. Generate Pygal chart
5. Convert to Base64 SVG
6. Return JSON response

## Infrastructure Architecture

### AWS CloudFormation Stack

```yaml
Resources:
  # Compute
  - LambdaFunction (Car-Bon API)
  - LambdaExecutionRole
  - LambdaFunctionURL
  
  # Storage
  - DynamoDBTable (CarBon_Data)
  - DynamoDBTable (user_table)
  - S3Bucket (Logs)
  
  # Security
  - IAMRole (Lambda execution)
  - IAMManagedPolicy (DynamoDB access)
  - SecretsManagerSecret
  
  # Monitoring
  - CloudWatchLogGroup
  - CloudWatchAlarm (DynamoDB capacity)
  - CloudWatchAlarm (Lambda errors)
  
  # Scaling
  - ApplicationAutoScaling (DynamoDB)
  - ScalingPolicy (Target tracking)
```

### Container Architecture

```dockerfile
FROM public.ecr.aws/lambda/python:3.10

# Base: AWS Lambda Python 3.10 runtime
# Size: ~400MB compressed

Layers:
1. Base OS (Amazon Linux 2)
2. Python 3.10 runtime
3. Application dependencies (pip install)
4. Application code (src/API)

Handler: app.index:handler (Mangum adapter)
```

## Security Architecture

### 1. Authentication & Authorization

**Current Implementation:**
- Function URL with public access
- API key authentication (planned)
- JWT tokens (planned)

**Best Practices:**
- Use AWS IAM for service-to-service auth
- Implement API Gateway with API keys
- Add OAuth 2.0 for user authentication

### 2. Data Encryption

**At Rest:**
- DynamoDB: AWS KMS encryption
- S3: Server-side encryption (SSE-KMS)
- Secrets Manager: Encrypted by default

**In Transit:**
- HTTPS/TLS 1.2+ for all API calls
- Encrypted WebSocket connections
- Twilio API over HTTPS

### 3. Secrets Management

```python
# Production: AWS Secrets Manager
secrets = secretsmanager.get_secret("Car-Bon-Secrets")

# Stored Secrets:
# - DATABASE_CREDENTIALS
# - TWILIO_API_KEYS
# - API_KEYS
# - THIRD_PARTY_TOKENS
```

### 4. Network Security

**CORS Configuration:**
```python
allow_origins = [
    "https://production-domain.com",
    "http://localhost:3000"  # Development only
]
```

**Rate Limiting:**
- AWS API Gateway throttling
- DynamoDB capacity limits
- Lambda concurrency limits

## Scalability & Performance

### 1. Horizontal Scaling

**AWS Lambda:**
- Concurrent executions: Up to 1000 (configurable)
- Auto-scaling based on request volume
- Regional deployment for low latency

**DynamoDB:**
- On-Demand capacity mode
- Auto-scaling read/write units
- Global tables for multi-region

### 2. Caching Strategy

**Client-Side:**
- Browser caching for static assets
- Local storage for user preferences

**Server-Side:**
- DynamoDB DAX (planned)
- CloudFront CDN for static files
- API response caching

### 3. Performance Optimization

**Query Optimization:**
```python
# Efficient DynamoDB queries
- Use partition key + sort key
- Implement pagination
- Project only required attributes
- Use batch operations
```

**Lambda Optimization:**
- Provisioned concurrency for warm starts
- Optimize package size
- Reuse connections (Boto3 clients)
- Async operations where possible

### 4. Monitoring & Observability

**CloudWatch Metrics:**
- Lambda invocations, errors, duration
- DynamoDB consumed capacity
- API Gateway request count

**Custom Metrics:**
- CO reading frequency
- Alert response time
- User engagement metrics

**Logging:**
```python
# Structured logging
logger.info("CO reading received", extra={
    "device_id": device_id,
    "co_level": co_value,
    "timestamp": timestamp
})
```

### 5. Disaster Recovery

**Backup Strategy:**
- DynamoDB Point-in-Time Recovery (PITR)
- Daily backups to S3
- Cross-region replication (planned)

**Recovery Time Objective (RTO):** < 1 hour
**Recovery Point Objective (RPO):** < 5 minutes

## Technology Decisions

### Why FastAPI?
- **Performance**: ASGI-based, async support
- **Type Safety**: Pydantic validation
- **Documentation**: Auto-generated OpenAPI docs
- **Modern**: Python 3.9+ features

### Why DynamoDB?
- **Serverless**: No infrastructure management
- **Scalability**: Automatic scaling
- **Performance**: Single-digit millisecond latency
- **Cost**: Pay-per-request pricing

### Why AWS Lambda?
- **Serverless**: No server management
- **Cost-Effective**: Pay only for compute time
- **Scalability**: Automatic scaling
- **Integration**: Native AWS service integration

### Why Twilio?
- **Reliability**: 99.95% uptime SLA
- **Global**: Worldwide SMS/voice coverage
- **Features**: Rich API for notifications
- **Compliance**: HIPAA, SOC 2 certified

## Future Enhancements

1. **Multi-Region Deployment**
   - Deploy to multiple AWS regions
   - Route 53 for DNS failover
   - Global DynamoDB tables

2. **Machine Learning Integration**
   - Anomaly detection for CO patterns
   - Predictive maintenance alerts
   - SageMaker integration

3. **Enhanced Monitoring**
   - X-Ray distributed tracing
   - Custom CloudWatch dashboards
   - Real-time alerting with SNS

4. **API Gateway Integration**
   - Replace Function URLs with API Gateway
   - Advanced throttling and rate limiting
   - Usage plans and API keys

5. **Mobile App**
   - Native iOS/Android apps
   - Push notifications
   - Offline capability

---

*Last Updated: 2025-11-09*
*Version: 1.6.8*
