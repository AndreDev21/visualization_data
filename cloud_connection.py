import boto3
import charts

# Set AWS credentials using environment variables
import os
os.environ["AWS_ACCESS_KEY_ID"] = ""
os.environ["AWS_SECRET_ACCESS_KEY"] = ""

################################################
#Push the file to the AWS S3 bucket
################################################

s3 = boto3.resource('s3')
s3.meta.client.upload_file('bank_data.png', 'andre-first-bucket', 'bank_data.png', ExtraArgs={'ACL':'public-read'})

