import esp32
from machine import Pin
import utime


while True:
    # asi imprime en grados farenheit
    temperatura=esp32.raw_temperature()
    celsius=(temperatura-32)*(5/9)
    print(celsius)
    utime.sleep_ms(100)

