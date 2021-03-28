import requests
from pprint import pprint

def openWeatherApp(city):
    API_Key = '459198808d3b6256cef11c5d765cf109'
    lang = 'tr'
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city +"&lang="+lang +"&units=metric"
    weather_data = requests.get(base_url).json()
    pprint(weather_data)

if __name__ == '__main__':
    city = input("Enter a city : ")
    openWeatherApp(city)








#C:\Python39>python -m pip install --upgrade pip --user
#base_url ="http://api.openweathermap.org/data/2.5/weather?id=524901&appid="+ API_Key +"&lang="+lang
#base_url = "http://api.openweathermap.org/data/2.5/weather?" + API_Key + "&q=" + city +"&lang=" + lang
#base_url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&callback=test&appid="+API_Key