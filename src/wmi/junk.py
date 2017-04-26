import boto3 

from boto3 import client

conn = boto3.client(
    's3',
    aws_access_key_id='AKIAIWURGKTQ6F6RPPGQ',
    aws_secret_access_key='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',
)

#conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='web-map-interface', Prefix='maps/kenya/landcover')['Contents']:
    print(key['Key'])