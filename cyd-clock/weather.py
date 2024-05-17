import urequests

#Get weather information
def weather():
    weather = urequests.get('http://api.openweathermap.org/data/2.5/weather?q=Greensboro,NC,US&units=imperial&appid='+secrets.api)
    data = weather.json()

    return data