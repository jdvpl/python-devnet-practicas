from machine import Pin
import utime

#en la esp32 normal el led interno es el Numero 2 en la esp y la w es el 1
led_interno=Pin(4,Pin.OUT)

while True:
    led_interno.value(1)
    utime.sleep(1)
    led_interno.value(0)
    utime.sleep(1)