from machine import Pin
import utime

led_interno=Pin(2,Pin.OUT)

while True:
    led_interno.value(1)