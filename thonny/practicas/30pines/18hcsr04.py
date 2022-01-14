from hcsr04 import HCSR04
from machine import Pin,I2C
from sh1106 import SH1106_I2C
import time

# pines
# pin d5  es el de echo hcsr04
# pin d18 es el de triger hcsr04
ancho=128
alto=64

i2c=I2C(0,scl=Pin(22),sda=Pin(21))
oled =SH1106_I2C(ancho, alto, i2c)

sensor = HCSR04(trigger_pin=5, echo_pin=18,echo_timeout_us=1000000)

while True:
    distance = sensor.distance_cm()
    distancia="Distancia:{:.2f}cm ".format(distance)
    print(distancia)
    time.sleep(1)
    oled.fill(0)
    oled.text(f"{distancia}:",0,0) 
    oled.show()
    









