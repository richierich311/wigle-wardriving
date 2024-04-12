import requests

# Define your Wigle API credentials
username = 'Rjones96'
password = 'Cancer2020@'

# Encode the credentials for use in the Authorization header
encoded_credentials = 'QUlEZDY3ZTcxZDU0MjAyYWEyOWI5YWExZmY0NWY5ZjEwMjE6ZTZlMzViMGZjZjViMDJkYTY4YmM0M2FiNmM3ODg5YmI='

# Define the URL for the Wigle API
url = 'https://api.wigle.net/api/v2/network/search'

# Define parameters for the API request
params = {
    'onlymine': 'true',  # Set to 'true' to search only networks uploaded by your account
}

# Make the API request
response = requests.get(url, params=params, headers={'Authorization': 'Basic ' + encoded_credentials})

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Process the data (e.g., print network names and their locations)
    for network in data['results']:
        print(f"SSID: {network['ssid']}, Latitude: {network['trilat']}, Longitude: {network['trilong']}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
