from machine import Pin, ADC, I2C
import utime
import sh1106
# i2c para la comunicacion de la pantalla

ancho=128
alto=64

i2c=I2C(0,scl=Pin(22),sda=Pin(21))
oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)

# escanea si quedo bien
print(i2c.scan())
# recibe el texto,posicion fila y columna

oled.fill(0)
oled.text('Juan Daniel', 0, 0) 
oled.text('Areandina', 0, 10) 
oled.text('Kakaroto', 0, 20) 



oled.show()
utime.sleep(4)

