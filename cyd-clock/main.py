#from ili9341 import Display, color565
#from xpt2046 import Touch
#from machine import Pin, SPI, SDCard, ADC, idle
#import network
#import time
import urequests
#import secrets
import json
import os
import wifi_manager as wifimgr 
#import utime
from cydr import CYD

#Initialize display
cyd = CYD()

#Launch WiFi Manager
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")
cyd.rgb(cyd.BLUE)
#Get weather information
weather = urequests.get('http://api.openweathermap.org/data/2.5/weather?q=Greensboro,NC,US&units=imperial&appid='+secrets.api)
data = weather.json()
temp = data['main']
disp = round(temp['temp'])
print(disp)
cyd.backlight.on()

#display functions
cyd.display.clear(cyd.YELLOW)
cyd.display.draw_text8x8(cyd.display.width //32,cyd.display.height //9,str(disp),cyd.WHITE,background=0)

