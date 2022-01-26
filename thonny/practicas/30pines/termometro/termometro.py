from lib.mlx90614 import MLX90614
from machine import I2C, Pin
import time

i2c =I2C(-1,scl=Pin(22), sda=Pin(21),freq = 100000)
sensor = MLX90614(i2c)

print("Ambient (C)", sensor.read_ambient_temp())
print("Object  (C)", sensor.read_object_temp())

if sensor.dual_zone:
    print("Dual zone")
    print(sensor.object2_temp)
else:
    print("Single zone")
print("Continuous sampling")
while True:
    print(sensor.read_object_temp())
    time.sleep_ms(1000)