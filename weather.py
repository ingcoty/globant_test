import json
import requests
from globant_test.mapper import ApiResponse, Encoder
from flask import Flask, request, Response
from flask_restful import Resource, Api
from flask_caching import Cache
from globant_test.config import forecast_url, weather_url, TOKEN

cache = Cache()
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
api = Api(app)
cache.init_app(app)

@cache.memoize(timeout=2000)
def getData(city, country):        
    apiresponse = requests.get(weather_url.format(city, country, TOKEN)).json()
    forecast = requests.get(forecast_url.format(city, country, TOKEN)).json()
    jsonObj = ApiResponse(json.dumps(apiresponse), forecast)
    jsonData = json.dumps(jsonObj, indent=4, cls=Encoder, ensure_ascii=False).encode('utf8')         
    resp = Response(jsonData, status=200)
    resp.headers["Content-Type"] = "application/json"        
    return(resp)


@app.route('/weather')
def get():    
    try:
        city = request.args.get('city')
        if not city:
            raise Exception("City is Required")
        country = request.args.get('country')  
        if not country:
            raise Exception("Country in Required") 
        resp = getData(city, country)
        return resp
    except Exception as e:        
        return Response({f'Bad Request : {str(e)}'}, status=400)


if __name__ == '__main__':
    app.run(debug=True)
    