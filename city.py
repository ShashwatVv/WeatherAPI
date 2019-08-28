import pyowm


owm = pyowm.OWM('a186f048c4365e79c02438c9dffb2295') #pyowm.OWM('API_KEY')
#This API_KEY is provided by https://openweathermap.org/

obs = owm.weather_at_place('Delhi')
weather = obs.get_weather()

temperature = weather.get_temperature(unit= 'celsius')['temp'] # unit = 'fahrenheit' (alternative option)

print('The Temperature is '+ str(temperature) + 'degrees Celsius' )
