from miniIO_S3.S3 import minio_client
from botocore.exceptions import ClientError


def get_photo_object(filename):
    return f"{filename}.jpg"

def upload_photo(filename, file_path, bucket_name):
    """
    Загружает аватар пользователя на MinIO.
    :param bucket_name:
    :param filename: str или int — id пользователя
    :param file_path: str — путь к локальному файлу аватарки
    """
    object_name = get_photo_object(filename)
    minio_client.upload_file(file_path, bucket_name, object_name)

def upload_photo_bytes(filename, img_bytes,bucket_name):
    """
    Загружает аватар пользователя на MinIO через boto3 из байтового потока.
    :param bucket_name:
    :param filename: str или int — id пользователя
    :param img_bytes: BytesIO — байтовый поток с фото
    """
    object_name = get_photo_object(filename)
    minio_client.upload_fileobj(
        img_bytes,
        bucket_name,
        object_name,
        ExtraArgs={'ContentType': 'image/jpg'}
    )

def download_photo(filename, download_path, bucket_name):
    """
    Скачивает аватар пользователя из MinIO.
    :param bucket_name:
    :param filename: str или int — id пользователя
    :param download_path: str — путь для сохранения аватарки
    """
    object_name = get_photo_object(filename)
    minio_client.download_file(bucket_name, object_name, download_path)

def get_photo_bytes(filename, bucket_name):
    object_name = get_photo_object(filename)
    try:
        response = minio_client.get_object(Bucket=bucket_name, Key=object_name)
        return response['Body'].read()
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return None
        else:
            raise
