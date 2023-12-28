# Import necessary modules 
import boto3
from pprint import pprint

# Create a management console 
aws_management_console = boto3.session.Session(region_name="us-east-1", profile_name="default")

# Create an ec2 client 
ec2_client = aws_management_console.client(service_name="ec2")

# Get the instance ID using describe_instances()
json_result = ec2_client.describe_instances()['Reservations']
#pprint(json_result)

# Print instanceID's
for each_instance in json_result: 
    for each_instanceId in each_instance['Instances']: 
        print(each_instanceId['InstanceId'])