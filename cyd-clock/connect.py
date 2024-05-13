import usocket as socket
import network
import secrets

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

networks = wifi.scan()

#Create WiFi Select Interface
html = "'<!DOCTYPE html><html><center><h1>WiFi Config</h1></center><form><h3>Please Select Your Network</h3><select name = "network" id = "network"><% var i; for i in networks{%><option name = "secrets.ssid" value = i>i</option>}%>'"

#Connect to network 
wifi.connect(secrets.ssid,secrets.wifiPswd)

#Initialize Socket
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

Host = ''
Port = 80
soc.bind((Host,Port))

soc.listen(1)