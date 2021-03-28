import requests
from pprint import pprint

def openWeatherApp(city):
    API_Key = '459198808d3b6256cef11c5d765cf109'

    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

    weather_data = requests.get(base_url).json()

    pprint(weather_data)

if __name__ == '__main__':
    city = input("Enter a city : ")
    openWeatherApp(city)








#C:\Python39>python -m pip install --upgrade pip --user