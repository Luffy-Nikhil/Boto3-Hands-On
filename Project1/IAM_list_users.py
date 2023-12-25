# Import boto3 module to access AWS
import boto3
from pprint import pprint

aws_management_console = boto3.session.Session(profile_name = "default")
# IAM client object 
iam_console_client = aws_management_console.client('iam') 

result = iam_console_client.list_users()
for user in result['Users'] : 
    print(user['UserName'])