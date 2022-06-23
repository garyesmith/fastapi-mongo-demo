"""
Routes for doing CRUD operations on post
"""

import tempfile
from typing import Tuple, List, Optional

#import aiohttp
from fastapi import APIRouter, HTTPException, Path, Query, status, Request

from config import settings
from models.pydantic.post import (
    Post
)
from utils.db import Database

from bson.objectid import ObjectId

router = APIRouter()

"""
Read routes
"""


@router.get(
    "/posts", 
    response_description="List all posts.", 
    response_model=List[Post]
)
async def list_posts(request: Request):
        
    print("List posts")
    post = await Database.db["post"].find({}).to_list(1000)
    return post

@router.get(
    "/posts/{id}", 
    response_description="Display one post record.", 
    response_model=Post
)
async def get_post(id: str, request: Request):

    try: 
        ObjectId(id)
    except:
      raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid ObjectId format.",
        )
         
    post = await Database.db["post"].find_one({"_id": ObjectId(id)})
    
    if post:
        return post
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No matching record found.",
        )

"""
Create routes
"""

@router.post(
    "/posts",
    response_description="Create a new Post record.", 
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Post,
)
async def create_post(post: Post, request: Request):

    if hasattr(post, 'id'):
        delattr(post, 'id')
    result = await Database.db["post"].insert_one(post.dict(by_alias=True))
    post.id = result.inserted_id
    return post

"""
Update routes
"""

@router.put("/posts/{id}",
    response_description="Update a Post record.", 
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_post(id: str, post: Post, request: Request):

    existing = await Database.db["post"].find_one({"_id": ObjectId(id)})
    if existing:
        post=post.dict(by_alias=True);
        del post['_id']
        updated_record = await Database.db["post"].update_one(
            {"_id": ObjectId(id)}, {"$set": post}
        )
        if updated_record:
            return True
        return False

"""
Delete routes
"""

@router.delete("/posts/{id}",
    response_description="Delete a Post record.", 
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_post(id: str, request: Request):

    existing = await Database.db["post"].find_one({"_id": ObjectId(id)})
    if existing:
        result = await Database.db["post"].delete_one({"_id": ObjectId(id)})
        if result.deleted_count==1:
            return True
        return False
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found.",
        )
