import requests
import json

# Replace with your API key
api_key = "e7602e0a5cc41c486b812006b0bcfa5b"
city = input("Enter city name: ")

# Construct the full URL for the API call
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response to a Python dictionary
    data = response.json()
    
    # Now you can work with the data
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    
    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error fetching data: {response.status_code}")
    print(response.text)