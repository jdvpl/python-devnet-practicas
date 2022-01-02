from machine import Pin
import utime

# pull down: va estar en estado 0 debe ir a psotivo
# pull up: va a estar en estado 1 debe ir a negativo
push=Pin(4,Pin.IN,Pin.PULL_UP)

led=Pin(18,Pin.OUT)
led19=Pin(19,Pin.OUT)
while True:
    estado=push.value()
    utime.sleep_ms(200)
    if estado==0:
        led.value(1)
        led19.value(1)
    else:
        led.value(0)
        led19.value(0)
    
    print(estado)
    