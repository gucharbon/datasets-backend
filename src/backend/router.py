"""

"""
from typing import List
from starlette.responses import Response, StreamingResponse
from fastapi import APIRouter
from fastapi import File as FileContent, UploadFile
from .models import Dataset, DatasetInDB, File, FileInDB
from .logger import get_logger
from .s3 import get_file, put_file


logger = get_logger(__name__)
router = APIRouter()


@router.get(
    "/datasets/", tags=["datasets"], status_code=200, response_model=List[DatasetInDB]
)
def list_datasets():
    """
    List all datasets in database that can be accessed (public datasets and private dataset accessible by the user)
    """
    # TODO: Query datasets in database
    return []


@router.post(
    "/datasets/",
    tags=["datasets"],
    status_code=202,
    response_model=DatasetInDB,
    response_description="Successfull dataset creation",
)
def create_dataset(body: Dataset):
    """
    Create a new dataset object into database
    """
    # TODO: Create dataset entry into database
    return dict(**body.dict(), id=1)


@router.get(
    "/datasets/{dataset_id}",
    tags=["datasets"],
    response_model=DatasetInDB,
    summary="Get dataset details",
    status_code=200,
    response_description="Successfull dataset read",
)
def get_dataset(dataset_id: int):
    """
    Return dataset informations such as name, description, and files details
    """
    # TODO: Fetch dataset from database
    return dict(id=1, name="demo")


@router.post(
    "/datasets/{dataset_id}/files",
    tags=["datasets"],
    response_model=FileInDB,
    summary="Create a new file into a dataset",
    status_code=202,
    response_description="Successfull file creation",
)
def create_dataset_file(file: File, dataset_id: int):
    """
    Create a file for a specific dataset
    """
    # TODO: Insert file into database
    return dict(**file.dict(), id=1)


@router.post(
    "/datasets/{dataset_id}/files/{file_id}/content",
    tags=["datasets"],
    summary="Upload file content",
    status_code=204,
    response_description="Successfull file upload",
)
async def upload_dataset_file(
    dataset_id: int, file_id: int, file: UploadFile = FileContent(...)
):
    """
    Upload content for an existing file insides dataset
    """
    filename = file.filename
    # TODO: Get dataset name from database
    object_name = "test/" + filename
    await put_file(object_name=object_name, file=file)
    return Response(content=None, status_code=204)


@router.get(
    "/datasets/{dataset_id}/files/{file_id}",
    summary="Get a file content by ID",
    tags=["datasets"],
    status_code=200,
    response_description="Successfull file read",
    response_class=StreamingResponse,
)
def get_dataset_file_by_id(dataset_id: int, file_id: int):
    """
    Get a dataset file content by ID
    """
    # TODO: Get dataset name and filename from database
    object_name = "test/2020-04-13-083325.jpg"
    # Get file from s3
    s3_response = get_file(object_name)
    # Stream response to client
    return StreamingResponse(s3_response.stream())
