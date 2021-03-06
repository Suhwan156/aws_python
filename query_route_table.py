#!/usr/bin/env python3

import json, boto3

region = 'ap-northeast-2'
vpc_name = 'mastering_kpython_networking_demo'

ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2')

response = client.describe_route_tables()
print(json.dumps(response['RouteTables'][0], sort_keys=True, indent=4))
