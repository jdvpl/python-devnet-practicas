from machine import Pin, ADC, PWM
import utime

# freq=50 varia el ciclo de trabajo
led=PWM(Pin(2),freq=50)
led_verde=PWM(Pin(4),freq=50)

# resolucion maxima de entrada 16 bits 65536
# resolucion maxima de salida es de 10 bits 1024
# metodo duty para ver el ciclo de trabajo
while True:
    # aumenta el brillo automaticamente con la frecuencia 
    for ciclo_trabajo in range(0,1024):
        led.duty(ciclo_trabajo)
        led_verde.duty(ciclo_trabajo)
        utime.sleep_ms(10)
        

