# This file must be imported to access D1 mini hardware and LAN connectivity

import esp

esp.osdebug(None)

import gc

#import webrepl

#webrepl.start()

gc.collect()

import time
import ssd1306
from machine import I2C, Pin, PWM
import dht12
import neopixel

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

sensor = dht12.DHT12()

button = Pin(0)

def polsador():
   return not(button.value())

freqs = {'do' : 523, 're' : 587, 'mi' : 669, 'fa' : 698, 'sol' : 784, 'la' : 880,  'si' : 988} 

def toca(nota):
   beeper = PWM(Pin(14), freq=freqs[nota], duty=512)
   time.sleep(0.5)
   beeper.deinit()

led = neopixel.NeoPixel(Pin(15, Pin.OUT), 7)

color = {'vermell' : (0x20, 0x00, 0x00) , 'groc' : (0x20, 0x20, 0x00),
  'verd' : (0x00, 0x20, 0x00), 'cyan' : (0x00, 0x20, 0x20),
  'blau' : (0x00, 0x00, 0x20),  'magenta' : (0x20, 0x00, 0x20),
  'blanc' : (0x20, 0x20, 0x20), 'apagat' : (0x00, 0x00, 0x00)}



# MQTT publishing from RNT. Complete project details at https://RandomNerdTutorials.com/micropython-mqtt-publish-dht11-dht22-esp32-esp8266/

from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network

ssid = 'jortsnet'
password = '9periodico'

mqtt_server = '192.168.1.60'
client_id = ubinascii.hexlify(machine.unique_id())


def connect_mqtt():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server)
  #client = MQTTClient(client_id, mqtt_server, user=your_username, password=your_password)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def read_sensor():
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      temp = (b'{0:3.1f},'.format(temp))
      hum =  (b'{0:3.1f},'.format(hum))
      return temp, hum
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')
    
