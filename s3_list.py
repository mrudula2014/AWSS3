#List s3 Buckets

import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response  = s3.list_buckets()
print( response )
print('Existing Buckets')
for bucket in response['Buckets']:
	print(f' {bucket["Name"]}' )
