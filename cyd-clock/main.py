from ili9341 import Display, color565
from xpt2046 import Touch
from machine import Pin, SPI, SDCard, ADC, idle
import network
import time
import urequests
import secrets
import json
import os
from wifi_manager import WifiManager
import utime
#import usocket as socket

wm = WifiManager()
wm.connect()

while True:
    if wm.is_connected():
        print('Connected!')
    else:
        print('Disconnected!')
    utime.sleep(10)

# Set up SPI for display
# Baud rate of 80000000 seems about the max
display_spi = SPI(1, baudrate=80000000, sck=Pin(14), mosi=Pin(13))

# Set up display
# The library needs a reset pin, which does not exist on this board
display = Display(display_spi, dc=Pin(2), cs=Pin(15), rst=Pin(15))

#Set up display backlight
backlight = Pin(21, Pin.OUT)


WHITE = color565(255, 255, 255)

#connect()
#display available networks
#print(networks)





#Get weather information
weather = urequests.get('http://api.openweathermap.org/data/2.5/weather?q=Greensboro,NC,US&units=imperial&appid='+secrets.api)
data = weather.json()
temp = data['main']
disp = round(temp['temp'])
print(disp)
backlight.on()

#display functions
display.clear(color565(255, 255, 0))
display.draw_text8x8(display.width //32,display.height //9,str(disp),WHITE,background=0)

