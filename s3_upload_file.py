#Program to Upload a file in the S3 Bucket

import logging
import boto3

s3 = boto3.client('s3');
bucket = 'jyothy312'
obj = 's3_list'
with open("s3_list.py","rb") as f:
	s3.upload_fileobj(f, bucket,obj, ExtraArgs={'ACL':'public-read'})
