import logging
import boto3
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_ec2_instance(
    ami_id: str = 'ami-0bbb06a93289ba5b7',  # Update to valid AMI ID
    instance_type: str = 't3.micro',
    key_name: str = 'user-datakey'  # Use one of your existing key pairs
) -> str:
    """Create an EC2 instance with the specified configuration."""
    ec2 = boto3.client('ec2')

    try:
        # Create EC2 instance
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'ec2-created-by-python'}]
            }]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
        logger.info(f"Created EC2 instance {instance_id}")
        return instance_id

    except ClientError as e:
        logger.error(f"Error creating EC2 instance: {e}")
        raise

def main():
    try:
        # Call the function to create an EC2 instance
        instance_id = create_ec2_instance()
        # Log success message
        logger.info(f"Successfully created EC2 instance: {instance_id}")
    except Exception as e:
        # Log error details
        logger.error(f"Instance creation failed: {e}")

if __name__ == "__main__":
    main()
