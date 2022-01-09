from machine import Pin, ADC, I2C
import utime
import sh1106
# i2c para la comunicacion de la pantalla

ancho=128
alto=64

i2c=I2C(0,scl=Pin(22),sda=Pin(21))
oled = sh1106.SH1106_I2C(ancho, alto, i2c)

# calibrar potenciometro
# es el vp
sensor=ADC(Pin(36))
#debe quedar atenua a 3v a 11db permite un rango de lectura entre 0v a 3.6v
sensor.atten(ADC.ATTN_11DB)
#colocar una resolucion de 10 bits
#  se debe colocar la misma resolucion que la de salida en este caso 10bit
sensor.width(ADC.WIDTH_12BIT)

led_rojo=Pin(2,Pin.OUT)
led_verde=Pin(4,Pin.OUT)
# escanea si quedo bien
print(i2c.scan())
# recibe el texto,posicion fila y columna

while True:
    oled.fill(0)
    # sensor
    leectura=sensor.read()
    factor_dos=100/4096
    voltaje=factor_dos*leectura
    print(f"Voltaje {voltaje}")
    if voltaje <50:
        led_rojo.value(1)
        led_verde.value(0)
    else:
        led_verde.value(1)
        led_rojo.value(0)
    # mostrar en pantalla
    oled.text('Voltaje', 0, 0,1) 
    oled.text(str(voltaje), 0, 10,1) 
    oled.fill_rect(1,20,int(voltaje),25,1)
    oled.show()
    utime.sleep_ms(100)
