import boto3


def create_image_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Detected_Labels',
        KeySchema=[
            {
                'AttributeName': 'Label',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'Confidence',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Label',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Confidence',
                'AttributeType': 'N'
            }

        ],
	ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table


if __name__ == '__main__':
    image_table = create_image_table()
    print("Table status:", image_table.table_status)
