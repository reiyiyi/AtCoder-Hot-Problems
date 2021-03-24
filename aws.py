import os
import boto3

def get():
    #s3 = boto3.resource('s3')

    #'''
    s3 = boto3.resource('s3',
                aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
                region_name=os.environ["REGION_NAME"])
    #'''

    return s3

if __name__ == "__main__":
    s3 = get()
    print("success")