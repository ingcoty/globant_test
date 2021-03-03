import os

#end ponints Remote API
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}&units=metric&appid={}'
TOKEN=os.getenv("TOKEN")
