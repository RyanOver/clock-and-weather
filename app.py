from flask import Flask, render_template
import sys
import time
import requests
import json
import pytemperature
import threading
import googlemaps
from datetime import datetime
import pprint
import os

app = Flask(__name__)


@app.route('/')
def index():

  time_now = time.localtime()

  la_date = time.strftime("%A %d, %B %Y", time_now)

  weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=Montreal&appid=cc6566b18fb703c7c5f1928bd738a82c'
  weather = requests.get(weather_url)
  w = json.dumps(weather.json())
  x = json.loads(w)
  f = x['weather']
  temp = x['main']['temp']
  condition = f[0]['description']


  key='[API KEY]'
  origins = '[LONGITUDE], [LATITUDE]'
  destinations = '[LONGITUDE], [LATITUDE]'
  units = 'metric'
  mode = 'transit'
  # Arrival time to be every day at 15:50
  # 5 Hours = 18,000 seconds
  now = datetime.now()
  dt = datetime(now.year, now.month, now.day, 15, 55)
  arrival = time.mktime(dt.timetuple())
  arrival_time = arrival


  distance_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units={}&origins={}&destinations={}&arrivaltime={}&mode={}&key={}'.format(units, origins, destinations, arrival_time, mode, key)
  distance_raw = requests.get(distance_url)
  a = json.dumps(distance_raw.json())
  b = json.loads(a)
  c = b['rows'][0]['elements'][0]['duration']['value']
  duration_in_unix = int(c)
  leaving_time = int(arrival_time) - duration_in_unix
  leave = datetime.utcfromtimestamp(leaving_time).strftime('%H:%M')


  data = [
    {
    'date': la_date,
    'temp': round(pytemperature.k2c(float(temp))),
    'condition': condition,
    'leave': leave
    }
  ]

  return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
 