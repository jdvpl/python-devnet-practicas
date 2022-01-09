from machine import Pin
import utime

#en la esp32 normal el led interno es el Numero 2 en la esp y la w es el 1
led_cer=Pin(4,Pin.OUT)
led_rgb=Pin(21,Pin.OUT)

while True:
    led_cer.value(1)
    led_rgb.value(1)
    utime.sleep_ms(100)
    led_cer.value(0)
    led_rgb.value(0)
    utime.sleep_ms(100)