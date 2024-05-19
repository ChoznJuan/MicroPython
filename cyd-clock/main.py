#from ili9341 import Display, color565
#from xpt2046 import Touch
#from machine import Pin, SPI, SDCard, ADC, idle
#import network
import time
#import urequests
#import secrets
import json
import os
import wifimgr 
import weather as weather
import utime
from cydr import CYD

#Initialize display
cyd = CYD()

cyd.RGBr.off()
#cyd.backlight.on()
cyd.display.clear(cyd.YELLOW)
cyd.display.draw_text8x8(x=cyd.display.width - 15,y=cyd.display.height //10,text="'Connect to WiFi ssid ' + str(wifimgr.ap_ssid) + ', default password: ' + str(wifimgr.ap_password)",rotate=90,color=cyd.WHITE,background=0)
cyd.display.draw_text8x8(x=cyd.display.width - 25,y=cyd.display.height //10,text="and access the ESP via your favorite web browser at 192.168.4.1.",rotate=90,color=cyd.WHITE,background=0)

#if wifimgr.wlan_sta.isconnected() is False:
#    while True:
#        cyd.RGBr.on()
#        time.sleep(0.5)
#        cyd.RGBr.off()
#        time.sleep(0.5)
        
#Launch WiFi Manager
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D
# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")
cyd.RGBr.on()
cyd.RGBb.off()

temp = weather.data['main']
disp = round(temp['temp'])
print(disp)
cyd.backlight.on()

#display functions
cyd.display.clear(cyd.YELLOW)
cyd.display.draw_text8x8(cyd.display.width //32,cyd.display.height //9,str(disp),cyd.WHITE,background=0)

