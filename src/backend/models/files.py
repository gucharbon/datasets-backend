"""
This module defines the representation of dataset files objects
"""
from typing import Optional
from pydantic import BaseModel
from pydantic import constr


class File(BaseModel):
    """
    A file uploaded by a user must have a name.
    Optionally user can give a description and a format.
    If format is not given by user then it is inferred.
    A validation error will be raised if format cannot be inferred.
    """

    name: constr(
        min_length=2, max_length=256,
    )
    description: Optional[constr(max_length=256,)] = None
    format: Optional[str] = None
    compression: Optional[str] = None


class FileInDB(File):
    """
    A file stored in database must have an ID and a size in bytes.
    """

    id: int
    bytes_size: int


# class CSVFile(File):
#     header: str = "infer"
#     delimiter: str = ","
#     names: Optional[str] = None
#     index_col: Optional[str] = None
#     prefix: Optional[str] = None
#     thousands: Optional[str] = None
#     decimal: Optional[str] = None
#     encoding: Optional[str] = None
#     dtype: Union[Type, str, Dict[str, Union[Type, str]]]


# class JSONFile(File):
#     orient: Optional[str] = None
#     typ: Optional[str] = "frame"
#     dtype: Union[Type, str, Dict[str, Union[Type, str]]]
