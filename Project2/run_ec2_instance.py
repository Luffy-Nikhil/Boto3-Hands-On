# Import all the required modules and libraries 
import boto3

# Create a boto3 session 
aws_management_console = boto3.session.Session(profile_name ="default")

# Create a ec2 client 
ec2_client = aws_management_console.client(service_name = "ec2")

# Run instance based on the parameters
response = ec2_client.run_instances(
    ImageId = "ami-0c7217cdde317cfec", 
    InstanceType = "t2.micro", 
    MaxCount = 1, 
    MinCount = 1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
           'Tags': [
               {
                   'Key': 'Name',
                   'Value': 'Boto3_Automated_VM2'
               },
           ]
       },
    ]
)

