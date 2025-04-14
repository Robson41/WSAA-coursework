'''Quiz Question:
You are tasked with fetching a list of books from the API at http://andrewbeatty1.pythonanywhere.com/books.

Write a Python script that sends a GET request to the API to fetch all the books in the database.

Send a GET request to http://andrewbeatty1.pythonanywhere.com/books.
After receiving the response:
If the request is successful (status code 200), print the list of books returned by the API.
If the request fails, print an error message and the raw response content.
This is a simple GET request, and the response will include the data of all books currently in the API.

PSEUDOCODE

1. IMPORT REQUEST AND JSON
2. DEFINE URL AS API VARIABLE ENDPOINT
3. USE GET REQUEST TO FETCH DATA FROM THIS API
4. USE VALIDATION TO PRINT OFF STATUSE CODE AND PRINT OUT THE RETURNED BOOKS
5. PRINT AN ERROR IF REQUEST FAILS WITH A RAW RESPONSE CONTENT
'''
import requests, json  # Import the necessary libraries: requests to make HTTP requests and json to handle JSON data

url = "http://andrewbeatty1.pythonanywhere.com/books"  # Define the URL where the API is hosted

response = requests.get(url)  # Make a GET request to the URL to fetch the list of books

if response.status_code == 200:  # Check if the status code of the response is 200, which means "OK" or "success"
    # If the request was successful, print the status code and the data returned from the API in JSON format
    print(f'Response was successful and {response.status_code} is returned. The book API returns the following data:  {response.json()}')

else:  # If the status code is not 200, it indicates an error
    # Print an error message with the returned status code if the request was unsuccessful
    print(f'Response was unsuccessful and {response.status_code} is returned.')
