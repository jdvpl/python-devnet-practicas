from machine import Pin
import utime

rojo=Pin(15,Pin.OUT)
amarillo=Pin(2,Pin.OUT)
verde=Pin(4,Pin.OUT)

def semaforo(r,a,g):
    rojo.value(r)
    amarillo.value(a)
    verde.value(g)
    utime.sleep(1)
    
while True:
    semaforo(1,0,0)
    semaforo(0,1,0)
    semaforo(0,0,1)
    semaforo(0,1,0)
    
if __name__==("__main__"):
    main()