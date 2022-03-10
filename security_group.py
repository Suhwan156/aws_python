#!/usr/bin/env python3

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

# 보안그룹 쿼리
response = ec2.create_security_group(GroupName='mpn_security_group', Description='mpn_demo_sg', VpcId=vpc_id)
security_group_id = response['GroupId']
data = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {'IpProtocol': 'tcp',
         'FromPort': 80,
         'ToPort': 80,
         'IpRnages': [{'CidrIp': '0.0.0.0/0'}]
         },
        {'IpProtocol': 'tcp',
         'FromPort': 22,
         'ToPort': 22,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
])
print('Ingress Successfully Set %s' % data)
# 보안그룹 설명
print(security_group_id)
