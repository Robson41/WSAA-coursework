'''
Write a program in python that will read a file from a repository, 

The program should then replace all the instances of the text "Andrew" with your name. 

The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

I do not need to see your keys (see lab2)

Handup: Push the program as assignment04-github.py to assignments repository.
'''
import requests
import base64
import json
from config import apikey
#from config import apikey as cfg  # The configuration file holds our GitHub access credentials

# Define the URL pointing to the specific file within the GitHub repository.
# The URL structure follows GitHub's API for repository contents.
url = "https://api.github.com/repos/Robson41/aprivateone/contents/wsaa-code.json"

# Retrieve the personal access token for accessing a private repository.
# The API key is stored in configuration file under the key "access_private_repo"
#apikey = cfg["access_private_repo"]

#GET the url using the apikey
response = requests.get(url, auth=('token', apikey))

# Output the HTTP status code to help with debugging.
print("Status code:", response.status_code)

# Parse the response content as JSON.
# The GitHub API returns a JSON response which includes several keys, one of which is "content".
content = response.json()

# Check if the request was successful and verify that the "content" key is present in the returned JSON.
# If these conditions are met, proceed to decode the file content.
if response.status_code == 200 and "content" in content:
    # The "content" field contains the file data encoded in Base64 format.
    encoded_content = content["content"]
    
    # Decode the Base64 string to get the original content of the file.
    # The decoded content is a JSON string, which can then be parsed into a Python object.
    decoded_content = base64.b64decode(encoded_content).decode('utf-8')
    decoded_content = decoded_content.replace('andrew', 'mark')  #Use replace function ro replace andrew with mark
    
    # Display message showing that the file was successfully retrieved from the repo
    print("File gathered from repo")
else:
    # If the API request was unsuccessful or the expected data is missing, output an error message.
    print("Something went wrong. Check your token or file path.")
    # Exit the script immediately since there is no file to work with.
    exit()

# Parse the decoded string, which contains the JSON file data, into a Python data structure (dictionary or list).
# This transformation enables us to manipulate the data directly.
data = json.loads(decoded_content)

# Define a local file path where we want to save the updated JSON data.
# This file will be created (or overwritten if it already exists) in the same directory as the script.
local_file_path = 'wsaa-code.json'

# Open the file in write mode ('w') to create or overwrite the file with the updated JSON data.
# The json.dump method is used to serialize the Python data structure back into a JSON formatted string.
# The 'indent' parameter ensures the output is well formatted and human-readable.
with open(local_file_path, 'w') as file:
    json.dump(data, file, indent=4)

# Print a success message indicating that the replacement has been completed and the file is saved.
print("Name updated from Andrew to Mark in wsaa-code.json")



















































