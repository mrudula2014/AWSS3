
#S3 functions(Upload/delete folder and singlr object
import os
import mimetypes
import boto3


s3 = boto3.client('s3')


# Function for create bucket
def create_mybucket():
    mybucket = input("Bucket name: ")
    location = {'LocationConstraint': 'eu-west-2'}
    s3.create_bucket(Bucket=mybucket,CreateBucketConfiguration=location)

def delete_mybucket( mybucket ):
    s3.delete_bucket(Bucket=mybucket)

def list_my_buckets():
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f' {bucket["Name"]}')

def list_my_objects(mybucket):
    response = s3.list_objects(Bucket=mybucket)
    # print(response)
    for data in response["Contents"]:
        print(data['Key'])


def delete_my_objects(mybucket):
    response = s3.list_objects(Bucket=mybucket)
    # print(response)
    for data in response["Contents"]:
        print(data['Key'])
        delete_my_file(mybucket,data['Key'])

def delete_my_objects(mybucket,myfolder):
    response = s3.list_objects(Bucket=mybucket)
    for data in response["Contents"]:
        obj = data['Key']
        if(obj == myfolder):
            delete_my_file(mybucket,obj)

def upload_my_file(mybucket,file_name):
    response = s3.upload_file(file_name,mybucket,file_name)
    print(response)

def delete_my_file(mybucket,file_name):
    response = s3.delete_object(Bucket=mybucket,Key=file_name)
    print(response)


def upload_folder(mybucket,my_dir):
    for root,_,files in os.walk(my_dir):
        for file in files:
            full_file = os.path.join(root,file)
            print(full_file)
            rel_file = os.path.relpath(full_file,my_dir)
            print(rel_file)
            content_type = mimetypes.guess_type(full_file)[0]
            print("Uploading ",full_file,"in ",rel_file)
            s3.upload_file(full_file,mybucket,'test/'+rel_file)

def delete_obj_folder(mybucket, folder):
    print("Deleting :",folder)
    response = s3.delete_object(Bucket=mybucket,Key=folder)
    print(response.keys)


def menu():
    print("0:CreateBucket")
    print("1:ListBuckets")
    print("2:ListObjects")
    print("3: Upload a file")
    print("4: Upload a folder")
    print("5: Delete a file")
    print("6: Delete a folder")
    print("7:Delete Bucket")
    print("Enter 0 to exit")


#mybucket = os.getenv('MYBUCKET')

ch = 10
while(ch):
    menu()
    ch = int(input("0-7:    "))
    if (ch == 0):
        create_mybucket()
    elif( ch == 1):
        list_my_buckets()
    elif (ch == 2):
        print("Input Bucket name to see the list of Objects : ")
        mybucket = input("Bucket name:")
        list_my_objects(mybucket)
    # Upload the file
    elif (ch == 3):
        mybucket = input("Bucket name:")
        file_name = input("File name:")
        upload_my_file(mybucket,file_name)
    # Upload the directory
    elif (ch == 4):
        base_dir = '/Users/jyothyrajs/Documents'
        mybucket = input("Bucket name:")
        dir_name = input("Directory:")
        my_dir = os.path.join(base_dir,dir_name)
        upload_folder(mybucket,my_dir)
    elif (ch == 5):
        mybucket = input("Bucket name:")
        file_name = input("File:")
        delete_my_file(mybucket,file_name)
    elif (ch == 6):
        mybucket = input("Bucket name:")
        dir_name = input("Directory:")
        delete_my_objects(mybucket,dir_name)
    elif (ch==7 ):
        mybucket = input("Bucket name:")
        delete_mybucket(mybucket)
    else:
        exit(0)





