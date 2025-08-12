import requests


#city = input("Enter your city that you want to check the weather for: ")

weather_url = "https://weather.com/weather/today/l/9cb4f62ff367974ef3b5c8cc2a3398e3ff19877feb918237ff8b5267f87f8ef2"


# Weather_At(city)

def Weather_At():
    url = weather_url
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Data retrieved!")
        weather_data = response.json()
        print(weather_data)
    
    else:
        print(f"Fail to retrieve data {response.status_code}")

    

Weather_At()