import boto3
iam=boto3.client('iam')

#create user
iam.create_user(UserName='test_suhwan')

#attach policy					#AdministratorAccess 정책 연결
iam.attach_user_policy(
 UserName='test_suhwan',
 PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)
