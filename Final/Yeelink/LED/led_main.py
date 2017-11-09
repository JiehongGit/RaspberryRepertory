import driver_gpio_led as led_gpio 
import time    
    
led_gpio.init(7)      
      
while True: 
    time.sleep(1)
    led_gpio.gpio_high(7)        
    time.sleep(1)
    led_gpio.gpio_low(7)

led.clean()
