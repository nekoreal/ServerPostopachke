import boto3
from botocore.exceptions import ClientError

from config import minio_config
from utils.logger import logger, make_log


BUCKET_NAMES = [
    "avatars",
    "recipesphotos"
]

minio_client = boto3.client('s3', **minio_config)

@logger(txtfile="inits.txt", printlog=True, raiseexc=True, time=True)
def init_s3():
    global minio_client
    minio_client = boto3.client('s3', **minio_config)

    for bucket_name in BUCKET_NAMES:
        try:
            minio_client.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            if e.response['Error']['Code'] != 'BucketAlreadyOwnedByYou':
                raise




