# Fetch version from CLI
version=$1
# Fetch Aws Id if passed
aws_id=$2
# Fetch AWS Profile
aws_profile=$3
# Set Default Region
region=eu-north-1
# Set Function Name
function_name=car-bon
if [ $aws_profile ]; then
    # Choose AWS Profile (eg. Car_Bon)
    export AWS_PROFILE=$aws_profile
fi
# AWS output to STDOUT
export AWS_PAGER="" 
if [ $aws_id ]; then
    # Set aws id as the one passed
    AWS_Account_ID=$aws_id
else
    # Fetch AWS Account ID 
    AWS_Account_ID=$(aws sts get-caller-identity --no-cli-pager | jq ".Account" | sed s@\"@@g)
fi
echo "Deploying on AWS Account : $AWS_Account_ID"
# Update poetry version
poetry version $version
# Generate latest requirements.txt
poetry export --without-hashes --format=requirements.txt > requirements.txt
# Export version as app_version
echo $version > ./app/app_version
# Build Docker image
docker buildx build -t $function_name:$version .
# login to ecr docker 
aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $AWS_Account_ID.dkr.ecr.$region.amazonaws.com
# Get the latest built Docker image id.
docker_image_id=$(docker images --filter=reference="$function_name:$version" --format "{{.ID}}")
# Tag the Docker Image to ECR Image
docker tag $docker_image_id $AWS_Account_ID.dkr.ecr.$region.amazonaws.com/$function_name:$version
# Push the Image to ECR
docker push $AWS_Account_ID.dkr.ecr.$region.amazonaws.com/$function_name:$version
# Update Lambda Version
aws lambda update-function-code --function-name $function_name --image-uri $AWS_Account_ID.dkr.ecr.us-east-1.amazonaws.com/$function_name:$version
