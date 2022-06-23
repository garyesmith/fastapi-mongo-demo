"""
Pydantic models for PyObjectId
This allows FastAPI/Pydantic to work with MongoDB _id fields
Necessary because fields beginning with underscores are not natively supported by FastAPI/Pydantic

"""

from bson import ObjectId

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')