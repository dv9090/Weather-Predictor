import requests
import json

api_key = "Your API Key"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    # Convert the JSON response to a Python dictionary
    data = response.json()
    

    temperature_C = round(data['main']['temp'])
    temperature_F = round((temperature_C * 9/5) + 32)
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    
    print(f"Current weather in {city}")
    print(f"Temperature: {temperature_C}°C, {temperature_F}°F")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error fetching data: {response.status_code}")
    print(response.text)
