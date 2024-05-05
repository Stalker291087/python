import boto3

old_Username = input("Type the username you want to edit: ")
new_Username = input("Type the new name for the user: ")

def update_user(old_username, new_username):
    iam = boto3.client('iam')
    
    response = iam.update_user(
        UserName = old_username,
        NewUserName = new_username
    )
    print(response)
    
update_user(old_Username, new_Username)
