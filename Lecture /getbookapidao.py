
 # Import the requests library to make HTTP requests
import requests

# Define the URL of the API endpoint that returns book data
url = "http://andrewbeatty1.pythonanywhere.com/books"

# Define a function to get all books from the API
def get_all_books():
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Parse the response body as JSON and return it
    return response.json()

# This block runs only if the script is executed directly (not imported)
if __name__ == "__main__":
    # Call the function to get all books and print the result
    print(get_all_books())


def get_book_by_id(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

if __name__ == "__main__":
    print(get_book_by_id(123))

'''url = "http://andrewbeatty1.pythonanywhere.com/books"

def get_book_by_id(book_id):
    geturl = f"{url}/{book_id}"
    response = requests.get(geturl)

    # Print status and raw response for debugging
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    # Only try to parse JSON if status is OK (200)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status {response.status_code}"}

if __name__ == "__main__":
    print(get_book_by_id(1))'''

'''def get_all_books():
    response = requests.get(url)
    print("Status Code:", response.status_code)

    try:
        books = response.json()
        for book in books:
            print(f"ID: {book.get('id')}, Title: {book.get('title')}")
        return books
    except Exception as e:
        return {"error": f"Failed to fetch books: {e}"}'''


'''mport requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def get_all_books():
    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print("Raw Response Text:\n", response.text)

        # Try to parse JSON if status is OK
        if response.status_code == 200:
            books = response.json()
            print("Books Found:")
            for book in books:
                print(f"ID: {book.get('id')}, Title: {book.get('title')}")
            return books
        else:
            return {"error": f"Failed with status {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {e}"}

if __name__ == "__main__":
    get_all_books()
'''
'''from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/book/<title>')
def get_book_by_title(title):
    # your code here, like querying a book dictionary or DB
    return jsonify({'title': title, 'message': 'Book found!'})
'''













