from machine import Pin, ADC
import utime

#potenciomentro pin 36
# se calibra deacuerdo a las especificaciones del sensor
sensor=ADC(Pin(36))
#debe quedar atenua a 3v a 11db permite un rango de lectura entre 0v a 3.6v
sensor.atten(ADC.ATTN_11DB)
#colocar una resolucion de 12 bits
sensor.width(ADC.WIDTH_12BIT)

# ejemplo para temperatura si fuera el sensor dht11 en vez del potenciometro
#sensor tempratura 0 y 100 grados

while True:
    #read_u16: mide voltaje tienes hasta 16 bits
    #read: mide la tension de voltaje que deja pasar maximo 2^12=4096 12 bits
    lectura=sensor.read()
    factor_conversion=100/4096
    temp=factor_conversion*lectura
    print(f"{temp}°")
    utime.sleep_ms(100)