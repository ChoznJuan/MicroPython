import time
import json
import os
from wifimgr import WifiManager
import weather as weather
import machine
import getTime
from cydr import CYD


#Initialize display
cyd = CYD()

cyd.RGBr.off()
#cyd.backlight.on()
cyd.display.clear(cyd.BLACK)
cyd.display.draw_text8x8(x=cyd.display.width - 15,y=cyd.display.height //10,text="'Connect to WiFi ssid ' + str(wifimgr.ap_ssid) + ', default password: ' + str(wifimgr.ap_password)",rotate=90,color=cyd.WHITE,background=0)
cyd.display.draw_text8x8(x=cyd.display.width - 25,y=cyd.display.height //10,text="and access the ESP via your favorite web browser at 192.168.4.1.",rotate=90,color=cyd.WHITE,background=0)
        
#Launch WiFi Manager
wm = WifiManager()
wm.connect()

while True:
  if wm.is_connected():
    print("ESP OK")
    getTime()
    cyd.RGBr.on()
    cyd.RGBb.off()

    temp = weather.data['main']
    disp = round(temp['temp'])
    print(disp)
    print(getTime())
    cyd.backlight.on()

    #display functions
    cyd.display.clear(cyd.BLACK)
    cyd.display.draw_text8x8(cyd.display.width //32,cyd.display.height //9,str(disp),cyd.WHITE,background=0)
  else:
    cyd.display.clear(cyd.RED)
    cyd.display.draw_text8x8(cyd.display.width //32,cyd.display.height //9,"Not Connected to WiFi.",cyd.WHITE,background=0)