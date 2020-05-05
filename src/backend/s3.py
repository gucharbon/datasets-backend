"""
s3 module of datasets package
"""
import time
from typing import Optional
from urllib3.response import HTTPResponse
from minio import Minio
from minio.error import BucketAlreadyOwnedByYou
from fastapi import File
from .config import SETTINGS
from .logger import get_logger


logger = get_logger(__name__)


DATASETS_BUCKET = SETTINGS.s3.datasets_bucket

client: Optional[Minio] = None


def connect(**kwargs) -> Minio:
    """
    Return a new minio client based on given endpoints and credentials
    """
    global client
    client = Minio(
        SETTINGS.s3.endpoint,
        access_key=SETTINGS.s3.access_key,
        secret_key=SETTINGS.s3.secret_key,
        secure=SETTINGS.s3.secure,
        **kwargs,
    )
    logger.debug(
        f"Successfully connected to S3 server on endpoint: {SETTINGS.s3.endpoint}"
    )


def create_bucket() -> None:
    """
    Create the bucket where all datasets will be stored
    """
    try:
        client.make_bucket(DATASETS_BUCKET)
    except BucketAlreadyOwnedByYou:
        logger.debug(f"Not creating bucket {DATASETS_BUCKET}: Bucket already exists")
        pass
    else:
        logger.debug(f"Successfully created bucket {DATASETS_BUCKET}")


def get_file(object_name: str, **kwargs) -> HTTPResponse:
    """
    Retrieve an object from datasets bucket
    """
    data = client.get_object(DATASETS_BUCKET, object_name, **kwargs)
    return data


async def put_file(object_name: str, file: File, **kwargs) -> str:
    """
    Put an object into datasets bucket
    """
    # TODO: Do not read file but rather stream content as it comes
    await file.read()
    # Get the synchronous file interface from the asynchronous file
    file_obj = file.file
    # Store position of cursor (number of bytes read)
    file_size = file_obj.tell()
    # Reset cursor at start of file
    file_obj.seek(0)
    # Trace file upload with its size
    logger.debug(f"Uploading file: {object_name} with {file_size} bytes")
    # Time file upload for debug
    start = time.time()
    # Store object on s3 storage
    client.put_object(
        bucket_name=DATASETS_BUCKET,
        object_name=object_name,
        length=file_size,
        data=file_obj,
    )
    end = time.time()
    # Log time spent
    logger.debug(f"Took {end - start} seconds to upload {file_size} bytes")
