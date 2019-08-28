import pyowm


owm = pyowm.OWM('a186f048c4365e79c02438c9dffb2295')

obs = owm.weather_at_place('Delhi')
weather = obs.get_weather()

temperature = weather.get_temperature(unit= 'celsius')['temp']

print('The Temperature is '+ str(temperature) + 'degrees celsius' )
