import datetime
import json
from collections import namedtuple
from json import JSONDecoder, JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):        
        return(o.__dict__)


class ApiResponse:
    
    def __init__(self, jsonResponse, forecast):        
        obj = json.loads(jsonResponse, object_hook=self.customDecoder)
        self.location_name = obj.name
        self.temperature = obj.main.temp
        self.weather = '{}, {} m/s'.format(obj.weather[0].description,  obj.wind.speed)
        self.cloudiness = obj.weather[0].main
        self.pressure = '{} hpa'.format(obj.main.pressure)
        self.humidity = '{} %'.format(obj.main.humidity)
        self.sunrise = datetime.datetime.fromtimestamp(int(obj.sys.sunrise)).strftime('%H:%M')
        self.sunset = datetime.datetime.fromtimestamp(int(obj.sys.sunset)).strftime('%H:%M')
        self.geo_coordinates = [obj.coord.lat, obj.coord.lon]
        self.requested_time = datetime.datetime.fromtimestamp(int(obj.dt)).strftime('%Y-%m-%d %H:%M:%S')
        self.forecast = forecast

    def customDecoder(self, jsonData):
        return namedtuple('X', jsonData.keys())(*jsonData.values())
