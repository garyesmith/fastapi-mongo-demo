import base64
import json

from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from config import settings
from routers import post
from utils.db import Database

security = HTTPBearer()

#-------------------------------------------------------------------------
async def http_authorize(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    """
    Authorizes an HTTP request to a REST endpoint
    """
    if credentials.credentials != settings.api_key:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

#-------------------------------------------------------------------------


# instantiate web app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# include API routers for specialized REST endpoints
app.include_router(post.router, dependencies=[Depends(http_authorize)])

#-------------------------------------------------------------------------
@app.on_event("startup")
async def startup_event():
    """
    Carries out startup tasks:
    - Prints app version info
    - Initializes Mongo database connection.
      If this fails, it triggers shutdown
    """

    # builds app version info string
    version_string = " ".join(
        [
            "FASTAPI-REACT_FRAMEWORK",
            f"version {settings.version}; "
        ]
    )
    app.version_string = version_string
    print(app.version_string)

    # connecting to MongoDB
    is_db_initialized = await Database.initialize(
        settings.mongo_uri, settings.mongo_dbname
    )
    if not is_db_initialized:
        raise Exception("App failed to start. Shutting down...")

# API base endpoint
@app.get("/",
    response_description="Confirm the API is running.", 
    summary="API root",
    status_code=status.HTTP_202_ACCEPTED,
)
async def get():
    return JSONResponse({"status":"ok"})

