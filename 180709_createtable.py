from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb',region_name='ap-northeast-1')

table = dynamodb.create_table(
    TableName='',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  #Partition key
        },
        
        {
            'AttributeName': 'price',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'price',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 15,
        'WriteCapacityUnits': 15
    }
)

print("Table status:", table.table_status)
