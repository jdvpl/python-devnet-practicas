from machine import Pin, ADC
import utime

#potenciomentro
sensor=ADC(Pin(36))

while True:
    #read_u16: mide voltaje tienes hasta 16 bits
    #read: mide la tension de voltaje que deja pasar maximo 2^12=4096 12 bits
    
    lectura=sensor.read_u16()
    print(lectura)
    utime.sleep_ms(100)