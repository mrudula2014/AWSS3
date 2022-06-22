#Interacting with resource to AWS API
import boto3

print("Using Resource")
s3 = boto3.resource('s3')
bucket = s3.Bucket('jyothy312')

for obj in bucket.objects.all():
    print(obj.key,obj.last_modified)

#Access client from Resource
print("Using Client")
client = boto3.resource('s3').meta.client
response = client.list_objects(Bucket = 'jyothy312' )
for content in response['Contents']:
    obj_dict = client.get_object(Bucket = 'jyothy312', Key=content['Key'] )
    print(content['Key'],obj_dict['LastModified'])