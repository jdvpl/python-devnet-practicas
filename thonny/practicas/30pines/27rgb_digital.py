from machine import Pin
import utime

red=Pin(15, Pin.OUT)
green=Pin(2,Pin.OUT)
blue=Pin(4,Pin.OUT)

def leds(a,b,c):
    red.value(a)
    green.value(b)
    blue.value(c)

while True:
    leds(0,0,0)#apagado
    utime.sleep(1)
    leds(0,0,1)#azul
    utime.sleep(1)
    leds(0,1,0)
    utime.sleep(1)
    leds(0,1,1)
    utime.sleep(1)
    leds(1,0,0)
    utime.sleep(1)
    leds(1,0,1)
    utime.sleep(1)
    leds(1,1,0)
    utime.sleep(1)
    leds(1,1,1)
    utime.sleep(1)
    