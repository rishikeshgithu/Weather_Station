import requests

# API Key
api_key = "b1686e27e7a943dfa5e130559233010"

# Input the city name you want
city_name = input("Enter the city name: ")

# Define the URL with the provided API key and city name
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print all data
    for key, value in data.items():
        print(f"{key}: {value}")

    
else:
    print(f"Request failed with status code: {response.status_code}")
