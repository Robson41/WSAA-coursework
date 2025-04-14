import requests
import json

# Function to fetch data from the CSO API
def fetch_cso_data():
    # URL of the CSO API endpoint (for population data example)
    url = "https://ws.cso.ie/public-api/restful/PXData.q?mine_API_read_data&dataset=FP001&json=true"
    
    # Send GET request to fetch data
    response = requests.get(url)
    
    # If request was successful, return the JSON data
    if response.status_code == 200:
        return response.json()
    else:
        # Print an error if the request fails
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        return None

# Function to process and extract population data from the CSO response
def process_population_data(data):
    # Check if data exists
    if data: #THIS MEANS IF THE DATA HAS SOMETHING IN IT, IN OTHER WORDS IF IT'S NOT EMPTY DO THE BELOW. If you are wondering where data is defined, it's defined in the main script at the bottom, which gets called first, before the other functions get executed. We can see that the fetch_cso_data() function returns json data and in the main funciton it says if json data gets returned, assign it in to the process_population_data function. And then in the process_population_data itself, we can see that the variable data is passed, which we know form above, is now defined as a dictionary.
        # Extract the relevant information from the response
        values = data.get('value', [])
        dimensions = data.get('dimension', {})

        # Extract dimension details (e.g., years, gender, counties)
        years = dimensions.get('statistic', {}).get('label', [])#NESTED DICTIONARIES - IT'S BETTER TO HAVE A .GET ON A .GET IN THIS SCENARIO
        genders = dimensions.get('sex', {}).get('label', [])
        counties = dimensions.get('county', {}).get('label', [])
        
        # Initialize a dictionary to hold the parsed data
        population_data = {}
        
        # We need to loop through the values, which are multidimensional
        # Assume the order is Year -> Gender -> County (as mentioned in the description)
        index = 0
        
        # Loop through each year
        for year in years:
            population_data[year] = {}# This is assigning an empty dictionary to each year(key) in the population_data dictionary. You use an empty dictionary ({}) as a placeholder to store data later. It's like setting up an empty box that you plan to fill with specific information (in this case, population data) as your code runs. You can access the value associated with a particular key by using square brackets []. This is called indexing or key-based access.In this case, the value is an empty dictionary ({}), and you're setting population_data[year] = {}.
            
            # Loop through each gender - same for gender
            for gender in genders:
                population_data[year][gender] = {}
                
                # Loop through each county 
                for county in counties:
                    # Each value corresponds to a specific (year, gender, county) combination
                    population_data[year][gender][county] = values[index]#The values list contains data points corresponding to specific (year, gender, county) combinations. The code assigns each element from values to the appropriate position in the population_data dictionary, incrementing the index as it loops through each year, gender, and county.
                    
                    # Move to the next index in the values array
                    index += 1
        
        # Return the parsed population data
        return population_data
    else:
        # Return an empty dictionary if no data is available
        return {}

# Function to display the parsed data
def display_population_data(population_data):
    # Display the population data in a readable format
    for year, year_data in population_data.items(): #The .items() method allows you to iterate over a dictionary, returning both the key and its value as pairs. In your code, it's used in nested loops to access data in a hierarchical structure (year → gender → county → population), making it easier to display the information in a readable format.
        print(f"Year: {year}")
        
        for gender, gender_data in year_data.items():
            print(f"  Gender: {gender}")
            
            for county, population in gender_data.items():
                print(f"    County: {county} | Population: {population}")

# Main function to fetch, process, and display CSO data
def main():
    # Fetch the CSO data
    cso_data = fetch_cso_data()
    
    # Process the population data if fetched successfully
    if cso_data:
        population_data = process_population_data(cso_data)
        
        # Display the processed data
        display_population_data(population_data)

# Run the main function
if __name__ == "__main__":
    main()
