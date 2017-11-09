# -*- coding: utf-8 -*-  
import requests  
import time  
import RPi.GPIO as GPIO    


# 设备URI, 在创建的温度传感器处查看自己的传感器apiurl替换下面的路径
apiurl = 'http://api.yeelink.net/v1.1/device/356749/sensor/406525/datapoints'  
# 用户密码  
apiheaders = {'U-ApiKey': '163adeb9ab915260830124d9ebc2f8c5'} 


def init(gpiox):   
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpiox,GPIO.OUT)       
       
def gpio_high(gpiox):   
    GPIO.output(gpiox, GPIO.HIGH)    
       
def gpio_low(gpiox):    
    GPIO.output(gpiox, GPIO.LOW)        
       
def clean():    
    GPIO.cleanup()

led = init(7)  

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
    gpio_high(7) 
  else:  
    print("led off")  
    gpio_low(7)  
  # 延时1S  
  time.sleep(1)    
led.clean()
