import pyowm


owm = pyowm.OWM('API_KEY')#replace  API_KEY with your authentic API_KEY
obs = owm.weather_at_id(#cityId)
weather = obs.get_weather()
temperature = weather.get_temperature(unit='fahrenheit')['temp']

print('The temperature is ' + str(temperature) + ' degrees Fahrenheit.')
