"""
Pydantic models for Post

*IMPORTANT* These are **not** database models. They are only used by the API routes. FastAPI uses Pydantic to parse and validate request and response data automatically when these models are used in the route definitions.
"""

from datetime import datetime
from enum import Enum
from typing import Tuple, List, Dict, Optional

from pydantic import AnyUrl, BaseModel, ValidationError, Field, BaseConfig, Extra
from bson import ObjectId
from typing import Optional
from models.pydantic.py_object_id import PyObjectId

import motor.motor_asyncio

class Post(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    uri: str
    title: str
    excerpt: str
    body: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
