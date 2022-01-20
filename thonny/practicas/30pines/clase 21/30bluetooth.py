from machine import Pin
import ubluetooth
from BLE import BLEUART

led=Pin(4,Pin.OUT)

name="Espjdvpl"
ble=ubluetooth.BLE()
uart=BLEUART(ble,name)

def on_rx():
    rx_recibe=uart.read().decode().strip()
    uart.write("Espjdvpl dice: "+str(rx_recibe)+ "\n")

    if rx_recibe=="on":
        led.value(1)
        print("turning on lights..")
        uart.write("Espjdvpl dice: Encendiendo led. \n")
    elif rx_recibe=="off":
        led.value(0)
        print("turning off lights..")
        uart.write("Espjdvpl dice: Apagando led. \n")
    
uart.irq(handler=on_rx)