import boto3

username = input("Type the user name to be created: ")

def create_user(UserName):
    iam = boto3.client('iam')
    response = iam.create_user(UserName = username)
    print(response)


create_user(username)
