"""
Test file for module '/src/models/datasets.py'
"""
import pytest
from pydantic import ValidationError

from backend.models import Dataset
from backend.models.datasets import DatasetVisibility


def test_default():
    dataset = Dataset(name="demo")
    assert dataset.visibility == DatasetVisibility.PUBLIC
    assert dataset.visibility == "public"
    assert dataset.description is None


def test_private_visibility():
    dataset = Dataset(name="demo", visibility="private")
    assert dataset.visibility == DatasetVisibility.PRIVATE
    assert dataset.visibility == "private"


def test_public_visibility():
    dataset = Dataset(name="demo", visibility="public")
    assert dataset.visibility == DatasetVisibility.PUBLIC
    assert dataset.visibility == "public"


def test_visibility_validation_error():
    with pytest.raises(ValidationError):
        Dataset(name="demo", visibility="something_else")


def test_name_missing_error():
    with pytest.raises(ValidationError):
        Dataset(visibility="something_else")


def test_name_too_short():
    """ Ensure that dataset names with length < 2 lead to validation error """
    min_length = 2
    Dataset(name="a" * min_length)
    for i in range(min_length):
        with pytest.raises(ValidationError):
            Dataset(name="a" * i)


def test_name_too_long():
    """ Ensure that dataset names with length superior to 64 lead to validation error """
    max_length = 64
    Dataset(name="a" * max_length)
    with pytest.raises(ValidationError):
        Dataset(name="a" * (max_length + 1))


def test_description_too_long():
    """ Ensure that dataset descriptions with length > 256 lead to validation error """
    max_length = 256
    Dataset(name="demo", description="a" * max_length)
    with pytest.raises(ValidationError):
        Dataset(name="demo", description="a" * (max_length + 1))


def test_empty_description():
    """ Ensure that an empty description is allowed """
    Dataset(name="demo", description="")
