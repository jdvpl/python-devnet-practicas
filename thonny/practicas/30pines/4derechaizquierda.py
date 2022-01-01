from machine import Pin
import utime

pin16=Pin(16,Pin.OUT)
pin15=Pin(15,Pin.OUT)
pin2=Pin(2,Pin.OUT)
pin4=Pin(4,Pin.OUT)
pin17=Pin(17,Pin.OUT)
pin5=Pin(5,Pin.OUT)
pin18=Pin(18,Pin.OUT)
pin19=Pin(19,Pin.OUT)
# lista
leds=[pin16,pin15,pin2,pin4,pin17,pin5,pin18,pin19]

def derecha():
    for element in leds[::-1]:
        element.value(1)
        utime.sleep_ms(50)
        element.value(0)
        utime.sleep_ms(50)

def izquierda():
    for element in leds[::1]:
        element.value(1)
        utime.sleep_ms(50)
        element.value(0)
        utime.sleep_ms(50)


def ledswitch():
    derecha()
    utime.sleep_ms(1)
    izquierda()
    utime.sleep_ms(1)
    
while True:
    ledswitch()
    
if __name__==("__main__"):
    main()