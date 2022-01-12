from machine import Pin,  I2C
import utime
import sh1106
import dht


ancho=128
alto=64

i2c=I2C(0,scl=Pin(22),sda=Pin(21))
oled = sh1106.SH1106_I2C(ancho, alto, i2c)

file=open("dato.csv","w")

d=dht.DHT11(Pin(5))

while True:
    d.measure()
    oled.fill(0)
    print(f'Temperatura: {str(d.temperature())} Humedad: {str(d.humidity())}')
    oled.text(f'Temperatura: {str(d.temperature())}', 0, 0,1) 
    oled.text(f'Humedad: {str(d.humidity())}', 0, 10,1) 

    file.write(str(f'Temperatura: {str(d.temperature())} Humedad: {str(d.humidity())} \n'))
    
    file.flush()
    oled.show()
    utime.sleep_ms(100)

