# tests.py - Run a series of test queries against the API to verify functionality

import requests

# get all posts to determine the initial number of records to use as an index offset later
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
resp = requests.get(url, headers=headers)
initialPostCount = len(resp.json())
print("\n-------------------------------------------------------")
print("\nInitializing tests with " + str(initialPostCount) + " initial records in the post collection.")

# create a first post
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
body = {"uri": "first-post", "title": "First Post", "excerpt": "This is the first post on the blog.", "body": "<p>This is the first post on the blog.</p><p>This post lets us confirm  the <b>API</b> is working.</p>"}
print("\nCreating first post...")
resp = requests.post(url, headers=headers, json=body)
print("Response status code: " + str(resp.status_code))
if resp.status_code>=200 and resp.status_code<300:
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# count all posts to ensure insertion succeeded
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nCounting all posts to ensure insertion succeeded...")
resp = requests.get(url, headers=headers)
numPosts = len(resp.json())
print("Total records found: " + str(numPosts))
if numPosts==(initialPostCount+1):
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# create a second post
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
body = {"uri": "second-post", "title": "Second Post", "excerpt": "This is the second post on the blog.", "body": "<p>This is the second post on the blog.</p>"}
print("\nCreating second post...")
resp = requests.post(url, headers=headers, json=body)
print("Response status code: " + str(resp.status_code))
if resp.status_code>=200 and resp.status_code<300:
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# count all posts to ensure insertion succeeded
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nCounting all posts to ensure insertion succeeded...")
resp = requests.get(url, headers=headers)
numPosts = len(resp.json())
print("Total records found: " + str(numPosts))
if numPosts==(initialPostCount+2):
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# check first post title is correct
print("\nChecking first post title...")
respJson=resp.json()
firstPostId=respJson[initialPostCount]['_id']
firstPostTitle=respJson[initialPostCount]['title']
print("Post title: " + firstPostTitle)
if firstPostTitle=="First Post":
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# check second post title is correct
print("\nChecking second post title...")
respJson=resp.json()
secondPostId=respJson[initialPostCount+1]['_id']
secondPostTitle=respJson[initialPostCount+1]['title']
print("Post title: " + secondPostTitle)
if secondPostTitle=="Second Post":
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# update the second post
url ="http://localhost:8000/posts/"+secondPostId
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
body = {"uri": "second-post", "title": "Second Post Updated", "excerpt": "This is the second post on the blog.", "body": "<p>This is the second post on the blog.</p>"}
print("\nUpdating title of second post...")
resp = requests.put(url, headers=headers, json=body)
print("Response status code: " + str(resp.status_code))
if resp.status_code>=200 and resp.status_code<300:
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# get the second post
url ="http://localhost:8000/posts/"+secondPostId
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nGet the second post only...")
resp = requests.get(url, headers=headers)
respJson=resp.json()
secondPostTitle=respJson['title']
print("Post title: " + secondPostTitle)
if secondPostTitle=="Second Post Updated":
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# delete the second post
url ="http://localhost:8000/posts/"+secondPostId
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nDelete the second post...")
resp = requests.delete(url, headers=headers)
print("Response status code: " + str(resp.status_code))
if resp.status_code>=200 and resp.status_code<300:
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# count all posts to ensure deletion succeeded
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nCounting all posts to ensure deletion succeeded...")
resp = requests.get(url, headers=headers)
numPosts = len(resp.json())
print("Total records found: " + str(numPosts))
if numPosts==(initialPostCount+1):
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# delete the first post
url ="http://localhost:8000/posts/"+firstPostId
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nDelete the first post...")
resp = requests.delete(url, headers=headers)
print("Response status code: " + str(resp.status_code))
if resp.status_code>=200 and resp.status_code<300:
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

# count all posts to ensure deletion succeeded
url ="http://localhost:8000/posts"
headers={"Authorization":"Bearer your_api_key", "Content-Type": "application/json"}
print("\nCounting all posts to ensure deletion succeeded...")
resp = requests.get(url, headers=headers)
numPosts = len(resp.json())
print("Total records found: " + str(numPosts))
if numPosts==(initialPostCount):
	print("\033[92mPassed.\033[0m")
else:
	print("\033[91mFailed.\033[0m")

print("\nTests complete.")
print("\n-------------------------------------------------------")