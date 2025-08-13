import requests
from bs4 import BeautifulSoup


base_url = "https://weather.com/weather/today/l/d14a70242c8d79bf622ef26e82a35eeafa1643baea3abb51c3c0290a1fa1998e"

#city = input("Enter your city that you want to check the weather for: ")


def Weather_At():
    response = requests.get(base_url)

    if response.status_code == 200:
        print('Data retrieved successfully')
        BeautifulSoup(response.text, 'html.parser')
        

    else:
        print("Error fetching data from Weather.com API")



    

Weather_At()