# list all IAM users in AWS account

import boto3

aws_management_console = boto3.session.Session(profile_name = "default")
# Resource object
iam_console_resource = aws_management_console.resource("iam")  
# Client object
iam_console_client = aws_management_console.client("iam")

# List IAM users using resource object
for user in iam_console_resource.users.all():
    print(user.name)

# List IAM users using client object
for user in iam_console_client.list_users()["Users"]:
    print(user["UserName"])