#Interacting with client to AWS API
import boto3
client = boto3.client('s3')

response = client.list_objects(Bucket = 'jyothy312' )


for content in response['Contents']:
    obj_dict = client.get_object(Bucket = 'jyothy312', Key=content['Key'] )
    print(content['Key'],obj_dict['LastModified'])
