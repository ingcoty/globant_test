import json
import unittest
import requests_mock, requests
from globant_test import weather
from globant_test.fakedata import forecast_response, weather_response

@requests_mock.Mocker(kw="mock")
def test_getData(**kwargs):    
    kwargs["mock"].get('http://api.openweathermap.org/data/2.5/weather', json=weather_response, status_code=200)
    kwargs["mock"].get('http://api.openweathermap.org/data/2.5/forecast', json=forecast_response, status_code=200)
    resp = weather.getData('bogota', 'co')  
    jsonresp = json.loads(resp.data.decode('utf8'))
    assert(jsonresp['location_name'] == 'Bogotá')
    assert(jsonresp['temperature'] == 16)
    assert(jsonresp['weather'] == 'broken clouds, 2.06 m/s')
    assert(jsonresp['cloudiness'] == 'Clouds')
    assert(jsonresp['pressure'] == '1027 hpa')
    assert(jsonresp['humidity'] == '63 %')
    assert(jsonresp['sunrise'] == '06:07')
    assert(jsonresp['sunset'] == '18:09')
    assert(jsonresp['geo_coordinates'] == [4.6097, -74.0817])
    assert(jsonresp['requested_time'] == "2021-03-03 11:36:25")
