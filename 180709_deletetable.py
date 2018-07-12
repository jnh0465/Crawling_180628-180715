from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb',region_name='ap-northeast-1')

table = dynamodb.Table('')

table.delete()
