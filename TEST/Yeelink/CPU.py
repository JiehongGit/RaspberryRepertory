#!/usr/bin/env python  

import requests  
import json  
import time  

file = open("/sys/class/thermal/thermal_zone0/temp")  
CPUtemperature = float(file.read()) / 1000  
file.close

print "CPU Temperature :", CPUtemperature

topost_CPUtemperature_payload={'value':CPUtemperature}

url_CPUtemperature='http://api.yeelink.net/v1.1/device/356749/sensor/404450/datapoints' 
header={'U-ApiKey':'163adeb9ab915260830124d9ebc2f8c5', 'content-type': 'application/json'}

post_CPUtemperature = requests.post(url_CPUtemperature,headers=header,data=json.dumps(topost_CPUtemperature_payload))
