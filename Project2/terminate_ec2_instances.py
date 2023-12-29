# import required modules and libraries
import boto3

# Create a new session with boto3
aws_management_console = boto3.session.Session(profile_name = "default")

# Create a ec2 console 
ec2_client = aws_management_console.client(service_name = "ec2")

# stop ec2 instances
response = ec2_client.terminate_instances(
    InstanceIds=[
        'i-030dcf6bc4f773670',
    ]
)