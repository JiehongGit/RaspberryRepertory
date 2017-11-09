# -*- coding: utf-8 -*-  
import requests  
import time  
import driver_gpio_led
import led_main

# 设备URI, 在创建的温度传感器处查看自己的传感器apiurl替换下面的路径
apiurl = 'http://api.yeelink.net/v1.1/device/356749/sensor/406525/datapoints'  
# 用户密码  
apiheaders = {'U-ApiKey': '163adeb9ab915260830124d9ebc2f8c5'} 
 
led = led_main.led_gpio.init(7)  
while True:  
  #发送请求  
  r = requests.get(apiurl,headers=apiheaders)  
  # 打印响应内容  
  #print(r.text)  
  # 转换为字典类型 请注意 2.7.4版本使用r.json()  
  led_state = r.json()
  # {'value':x} x=1打开状态，x=0关闭状态  
  if led_state['value'] == 1:
    print("led on")  
    led_gpio.gpio_high() 
  else:  
    print("led off")  
    led_gpio.gpio_low()  
  # 延时5S  
  time.sleep(5)    
led.clean()
