#!/usr/bin/python
# --- DHT11 ---
# --- Author: dawmagoo.com ---
# --- Blog: dbook.me ---

#import biblioteki Adafruit potrzebnej nam do uruchomienia czujnika
import Adafruit_DHT

#określenie rodzaju czujnika jaki posiadamy, w tym przypadku jest to czujnik DHT11
sensor = Adafruit_DHT.DHT11
#gpio 4 oznacza iż czujnik jest połączony do pinu nr 4 na naszym raspberry pi 
gpio = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and temperature is not None:
    print('Temperatura={0:0.1f}*C  Wilgotnosc={1:0.1f}%'.format(temperature, humidity))
else:
    print('Blad odczytu z czujnika')