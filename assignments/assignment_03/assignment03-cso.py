import requests
import csv
import json

# URL for the Exchequer Account (Historical Series) CSV dataset
csv_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/en"

# Send a GET request to fetch the CSV file
response = requests.get(csv_url)

# Check if the request was successful (Status code 200)
if response.status_code == 200:
    print("Successfully retrieved the data.")

    csv_data = response.text # converting the data in to raw text data and storing it in the csv_data variable

    py_dict = csv.DictReader(csv_data.splitlines())# csv_data gets parsed in to a dictionary called py_dict is a dictionary that holds multiple items, each of which is a dictionary (representing a row of data).

    dictionary_lists = [row for row in py_dict]  # Convert to list of dictionaries because list will store the dictionaries and a list can be serilaized in to json. The list comprehension like data_list = [row for row in py_dict] creates a new list by iterating over each item in py_dict (which is an iterable of dictionaries -i.e.just iterates over the data, doesn't store it in a format).
    
    with open("cso.json", "wt") as f: # Creating a file object called cso.json and using with to close the filw
        json.dump(dictionary_lists, f) # Converting the file to json
    
    print("Data has been saved to 'cso.json'.") # Printing out result
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
