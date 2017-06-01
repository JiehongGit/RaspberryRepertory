#coding=utf-8
import RPi.GPIO as GPIO
import time
import picamera
from time import sleep
#from aa import main
 
#初始化
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37,GPIO.IN)
    GPIO.setup(13,GPIO.OUT)
    pass
 
#蜂鸣器鸣叫函数
def beep():
    while GPIO.input(37):
        GPIO.output(13,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(13,GPIO.HIGH)
        time.sleep(0.5)
#感应器侦测函数
def detct():
    #因为是仅仅试验，所以只让它循环运行100次
    for i in range(1,101):
        #如果感应器针脚输出为True，则打印信息并执行蜂鸣器函数
        if GPIO.input(37) == True:
            print "Someone isclosing!"
            
            with picamera.PiCamera() as camera:
                camera.resolution = (512, 384)
                camera.start_preview()
                camera.capture('foo.jpg')
                beep()
                #main()
                
        #否则将蜂鸣器的针脚电平设置为HIGH
        else:
            GPIO.output(13,GPIO.HIGH)
            print "Noanybody!"
        time.sleep(2)


 
time.sleep(5)
init()
detct()
#脚本运行完毕执行清理工作
GPIO.cleanup()
