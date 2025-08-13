import requests
from bs4 import BeautifulSoup


base_url = "https://weather.com/weather/today/l/d14a70242c8d79bf622ef26e82a35eeafa1643baea3abb51c3c0290a1fa1998e"

#city = input("Enter your city that you want to check the weather for: ")

html_text = requests.get(base_url).text
soup = BeautifulSoup(html_text, 'lxml')

temperature = soup.find('span', class_='TodayDetailsCard--feelsLikeTempValue--8WgHV').text
weather = soup.find('div', class_='CurrentConditions--phraseValue---VS-k').text

print(f"Current temperature: {temperature}")
print(f"Current weather: {weather}")