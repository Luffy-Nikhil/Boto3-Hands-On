# list all IAM users in AWS account

import boto3

aws_management_console = boto3.session.Session(profile_name = "default")
iam_console = aws_management_console.resource("iam")

for user in iam_console.users.all():
    print(user.name)