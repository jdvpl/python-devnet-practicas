from machine import Pin,  I2C
import utime
import sh1106
import dht


ancho=128
alto=64

i2c=I2C(0,scl=Pin(22),sda=Pin(21))
oled = sh1106.SH1106_I2C(ancho, alto, i2c)

data=Pin(5, Pin.IN)
d=dht.DHT11(data)

while True:
    d.measure()
    oled.fill(0)
    print(d.temperature())
    oled.text(f'Temperatura: {str(d.temperature())}', 0, 0,1) 
    oled.text(f'Humedad: {str(d.humidity())}', 0, 10,1) 
    oled.show()
    utime.sleep_ms(100)