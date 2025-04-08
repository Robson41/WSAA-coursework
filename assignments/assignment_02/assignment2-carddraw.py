import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1" # Define shuflle URL
response = requests.get(url)# Sending a GET request to the shuffle deck url
shuffle = response.json()# Retrieving the response and parsing it in to a json object
deck_id = shuffle["deck_id"]# Extract the deck id from the shuffle

url_2 = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5" #Define URL to draw five cards from the deck
response_2 = requests.get(url_2)# Sending a GET request to the URL
cards = response_2.json()# Retrieving the cards and parsing it in to a json object
drawn_cards = cards["cards"] # Extract the value and suit from each of the five cards

for card in drawn_cards: # For each card in the drawn cards
 print(f'The value of the card is {card['value']} and the suit is {card['suit']}') # Print the value and suit of each card drawn




