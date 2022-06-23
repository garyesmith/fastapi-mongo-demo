
# FastAPI with Mongo database demo

I had trouble finding a fully-functional demonstration that uses FastAPI to create a RESTful API that handles basic CRUD operations against a Mongo database.

One key challenge is that Mongo's default primary key fields are named `_id` but FastAPI/Pydantic does not permit field names in a model to begin with underscores. There was  much discussion of this problem in online forums, and several partially-described solutions, and the official Mongo documentation was recently updated to [describe a solution](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/) in full. 

This demonstration puts it all together to create a base repository that can be used to quickly spin up APIs in the future.

# Features
- Create, Read, Update and Delete against a model stored in a MongoDB collection.
- Validation using standard Pydantic model definitions.
- Connection to a Mongo database defined in `.env`.
- Authentication against a single secret Bearer Token defined in `.env`.
- Internal mapping of the Mongo `_id` field to `id` in code references.
- Clean separation of code for each endpoint router and model.
- Detailed automatic endpoint documentation generated via SwaggerUI.

# Prerequisites
This application has been tested against the following stack:
- Ubuntu 20
- Python 3.6
- A Mongo database (v4.4.15)
- python3-pip

# Installation

- Clone this repo and `cd` into the `fastapi-mongo-demo` folder
- Run `pip install -r requirements.txt`
- Create a new Mongo database 
- Optional: manually run the following Mongo query to create an initial record:
`db.post.insert({"uri":"first-post","title": "First Post", "excerpt": "This is the first post on the blog.", "body": "<p>This is the first post on the blog.</p><p>This post lets us confirm  the <b>API</b> is working.</p>"});`


# Configuration

- Copy or rename the file `.env-sample` in the application base folder to `.env`.
- Edit the file `.env` in the application base folder.
- Set the `MONGO_URI` value to be the connection string for your Mongo database (created above).
- Set the `MONGO_DBNAME` value to be the name of your Mongo database (created above).
- SET the `API_KEY` value to be a strong [random token string](https://www.random.org/strings/) known only to you.


# Usage

- From the application base folder, run the Uvicorn server:
  `python3 -m uvicorn main:app --reload --host="0.0.0.0" --port=8000`
- In a browser or Postman make a request to 
  `GET http://<server_ip_address>/posts` where `<server_ip_address` is the IP address of the server where this application is installed.
- Confirm you see the record inserted in the *Installation* step above


