import boto3
profile_name = "default"

session = boto3.Session(profile_name=profile_name,region_name="us-east-1")
print(session)
print(type(session))
print("-"*30)
_s3 = session.client(service_name="s3")
print(_s3)
print(type(_s3))
print("-"*30)
