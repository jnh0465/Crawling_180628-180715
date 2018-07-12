from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb',region_name='ap-northeast-1')

table = dynamodb.Table('')

def load(name):
    with open(name) as json_file:
        menus = json.load(json_file, parse_float = decimal.Decimal)
        for menu in menus:
            name = menu['name']
            price = menu['price']
    
            print("Adding menu:", name, price, )
    
            table.put_item(
               Item={
                   'name': name,
                   'price': price
                }
            )
            
load("_menu.json")
load("_menu2.json")
load("_menu3.json")
load("_menu4.json")
