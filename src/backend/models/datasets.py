"""

"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel, constr


class DatasetVisibility(str, Enum):
    """ A dataset visibility can either be 'public' or 'private' """

    PUBLIC: str = "public"
    PRIVATE: str = "private"


class Dataset(BaseModel):
    """
    Class representing a dataset. A dataset must have a name, and can
    optionnally have a description. It must also have a visibility level,
    which is public by default.
    """

    name: constr(
        min_length=2, max_length=64,
    )
    description: Optional[constr(max_length=256,)] = None
    visibility: DatasetVisibility = "public"


class DatasetInDB(Dataset):
    """
    A dataset in database must have an ID
    """

    id: int
