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
# funciones

def leds(a,b,c,d,e,f,g,h):
    pin16.value(a)
    pin15.value(b)
    pin2.value(c)
    pin4.value(d)
    pin17.value(e)
    pin5.value(f)
    pin18.value(g)
    pin19.value(h)


    
while True:
    leds(0,1,0,1,0,1,0,1)
    utime.sleep_ms(200)
    leds(1,0,1,0,1,0,1,0)
    utime.sleep_ms(200)
    leds(1,1,1,1,0,0,0,0)
    utime.sleep_ms(200)
    leds(0,0,0,0,1,1,1,1)
    utime.sleep_ms(200)
    
if __name__==("__main__"):
    main()