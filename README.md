
# FastAPI with Mongo database demo

A simple but fully-functional demonstration of using FastAPI to handle CRUD operations against a Mongo database.

One key challenge is that Mongo's default primary key fields are named `_id` but FastAPI/Pydantic does not permit field names in a model to begin with underscores. There was  much discussion of this problem in online forums, and several partially-described solutions; thankfully the official Mongo documentation was recently updated to [describe a proper solution](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/) in full. 

This demonstration puts it all together to create a base repository that can be used to quickly spin up APIs in the future.

# Features
- Perform Create, Read, Update and Delete on a model stored in a MongoDB collection.
- Validate fields using standard Pydantic model definitions.
- Connect to a Mongo database defined in `.env`.
- Authenticate all endpoints against a single secret Bearer Token defined in `.env`.
- Internally map the Mongo `_id` field to `id` in code and API calls.
- Cleanly separate code for each endpoint's router and model to enable easy future expansion.
- Automatically generate complete endpoint documentation via SwaggerUI.

# Prerequisites
This application has been tested with the following stack pre-installed:
- Ubuntu 20
- Python 3.6
- Mongo 4.4.15
- python3-pip

# Installation

- Clone this repo and `cd` into the `fastapi-mongo-demo` folder.
- Run `pip install -r requirements.txt` to install the required Python modules.


# Configuration

- Copy or rename the file `.env-sample` in the application base folder to `.env`.
- Edit the file `.env` in the application base folder.
  - Change the `MONGO_URI` value to be the connection string for a running Mongo database.
  - Change the `MONGO_DBNAME` value to be the desired name of your Mongo database.
  - Change the `API_KEY` value to be a strong [random token string](https://www.random.org/strings/) known only to you.
  - Save the file changes.


# Usage

- From the application base folder, run the Uvicorn server:
  
  `python3 -m uvicorn main:app --reload --host="0.0.0.0" --port=8000`

- In a browser visit `http://<server_ip_address>/docs` where `<server_ip_address>` is the IP address of the server where this application is installed.

- Confirm you see documentation describing the avaiable API endpoints.

- This demo provides CRUD endpoints for an endpoint called `/posts` for theoretical posts in a blog, which has the following model definition:

	```
    id: ObjectID
    uri: str
    title: str
    excerpt: str
    body: str
    ```

- To create an additional API endpoint, copy and modify `/models/pydantic/post.py` and `/routers/post.py` and use these as a base to define a model and routes specific to your new endpoint.


# Automated tests

Optionally, you may run a test script called located in the root folder of the application by executing this on the command line: `python3 tests.py`

This script runs a sequence of GET, POST, PUT and DELETE calls against the `/posts` endpoint and compares the returned values to ensure they are working as expected.




