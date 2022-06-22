import json
import urllib.parse
import boto3

def mydetect_labels(bucket,photo):
    
    rekog =boto3.client('rekognition') # type: botostubs.rekognition
    response = rekog.detect_labels(Image = {'S3Object' : {'Bucket': bucket, 'Name': photo}},MinConfidence=80,MaxLabels=3)
    print(response)
    #keep labels in dictionary
    result={}
    for labels in response['Labels']:
        result.update({labels['Name']:round(labels['Confidence'],2)})
    print('Detected labels for ',photo, result)

    return result

s3 = boto3.client('s3')
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        dyndb = boto3.resource('dynamodb')
        table = dyndb.Table('Detected_Labels')
        
        print('Bucket: ' + bucket + ' Key: ' + key)
        
        labels = mydetect_labels(bucket, key)
        conf = 0
        for label in labels:
            item = {}
            print("Label:", label)
            
            item['Label'] =  label
            curr_conf = int(labels[label])
            item['Confidence'] = curr_conf
            if( conf  < curr_conf):
                conf = curr_conf
                image = label
            print("Detected Item adding to db")
            print(item)
            
            table.put_item(Item=item)
        response = s3.get_object(Bucket=bucket, Key=key)
        MY_SNS_TOPIC_ARN = 'arn:aws:sns:eu-west-2:408474111132:s3Update'
        sns_client = boto3.client('sns')
        sns_client.publish(TopicArn = MY_SNS_TOPIC_ARN, Subject = 'S3 Update ' + bucket, Message = ' has changed by adding a file with name ' +key + ' and image is detected as ' + image)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
