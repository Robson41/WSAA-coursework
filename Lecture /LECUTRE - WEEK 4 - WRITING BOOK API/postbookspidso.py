'''Test Question:
You are tasked with creating a new book record through a POST request to the API at http://andrewbeatty1.pythonanywhere.com/books. The details of the book are as follows:

Title: "1984"
Author: "George Orwell"
Year: 1949
Your task is to:

Write a Python script that sends a POST request to the provided API to create the new book.
Make sure to include the necessary headers to indicate that you're sending JSON data.
After sending the POST request, check the response status code:
If the status code is 201, print a success message and the details of the newly created book.
If the status code is not 201, print an error message and the raw response content.
Let me know once you've written the code, and I'll be happy to review it!'''

'''PSEUDOCODE

1. IMPORT JSON AND REQUESTS
2. DEFINE URL WITH ENDPOINT
3. CREATE A DICTIONARY 
4. CREATE THE HEADER DICTIONARY TO ALLOW SERVER TO KNOW FORMAT OF POST
5. SEND POST REQUEST AND RETURN THIS TO RESPONSE OBJECT
6. CREATE VALIDATION TO CHECK POST HAS BEEN CREATED'''

import json, requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

book = {
"Title": "1984",
"Author": "George Orwell",
"Year": 1949
}

headers = { "Content-Type" : "application/json"

}

response = requests.post(url, json=book, headers=headers)

if  response.status_code == 201:
    print(f'Book has been successfully updated with {response.json()}' )

else:
    print(f'Post falied with {response.status_code} status code and response {response.text}')






































