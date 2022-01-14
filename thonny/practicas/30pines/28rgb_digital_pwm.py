from machine import Pin, PWM
import utime
from random import randint

red=PWM(Pin(15),freq=1000)
green=PWM(Pin(2),freq=1000)
blue=PWM(Pin(4),freq=1000)

while True:
    red.duty(randint(0,255)) #0 y 1023
    green.duty(randint(0,255))
    blue.duty(randint(0,255))
    
    utime.sleep(0.5)
    