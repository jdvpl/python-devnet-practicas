from machine import Pin, ADC, PWM
import utime

# calibrar
sensor=ADC(Pin(36))
#debe quedar atenua a 3v a 11db permite un rango de lectura entre 0v a 3.6v
sensor.atten(ADC.ATTN_11DB)
#colocar una resolucion de 10 bits
#  se debe colocar la misma resolucion que la de salida en este caso 10bit
sensor.width(ADC.WIDTH_10BIT)
# freq=50 varia el ciclo de trabajo
led_rojo=PWM(Pin(2),freq=500)
led_verde=PWM(Pin(4),freq=500)

# resolucion maxima de entrada 16 bits 65536
# resolucion maxima de salida es de 10 bits 1024
# metodo duty para ver el ciclo de trabajo
while True:
    # aumenta el brillo automaticamente con la frecuencia 
    # con el potenciometro varia el brillo del led
    ciclo_trabajo=sensor.read()
    led_rojo.duty(ciclo_trabajo)
    led_verde.duty(ciclo_trabajo)
    utime.sleep_ms(20)
    
        

