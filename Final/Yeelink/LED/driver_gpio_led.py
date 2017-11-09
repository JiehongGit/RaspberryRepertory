import RPi.GPIO as GPIO    
import time    
       
def init(gpiox):   
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpiox,GPIO.OUT)       
       
def gpio_high(gpiox):   
    GPIO.output(gpiox, GPIO.HIGH)    
       
def gpio_low(gpiox):    
    GPIO.output(gpiox, GPIO.LOW)        
       
def clean():    
    GPIO.cleanup()
