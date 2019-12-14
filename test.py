import sys
import time
import requests
import json
import pytemperature
import threading
import googlemaps
from datetime import datetime
import pprint


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

  now = datetime.now()
  dt = datetime(now.year, now.month, now.day, 15, 50)
  arrival = time.mktime(dt.timetuple())
  print(arrival)

  key='AIzaSyA_MT9mmCxgQYDC6YDY6a7t7PRK4HN1oms'
  origins = '45.616540, -73.625290'
  destinations = '45.499910, -73.570556'
  units = 'metric'
  mode = 'transit'
  arrival_time = '1574092500'
  
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
    'condition': condition
    }
  ]

  return

index()
