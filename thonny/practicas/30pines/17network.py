import machine
import sys
import network
import utime
import urequests

# Pines
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
repl_led = machine.Pin(5, machine.Pin.OUT)

# Network configuraciones
wifi_ssid = "Jdvpl"
wifi_password = "R@p1df@5t"

# url de una pagina
url = "https://jdvpl.com/"

# Create a station object to store our connection
station = network.WLAN(network.STA_IF)
station.active(True)

# Continually try to connect to WiFi access point
while not station.isconnected():

    # Try to connect to WiFi access point
    print("conectando...")
    station.connect(wifi_ssid, wifi_password)

    # Check to see if our REPL button is pressed over 10 seconds
    for i in range(100):
        if repl_button.value() == 0:
            print("Dropping to REPL")
            repl_led.value(1)
            sys.exit()
        utime.sleep_ms(100)

# Continually print out HTML from web page as long as we have a connection
while station.isconnected():

    # Display connection details
    print(f"conectada a la red {wifi_ssid}")
    print("Mi Direccion IP:", station.ifconfig()[0])

    # Perform HTTP GET request on a non-SSL web
    response = urequests.get(url)



    # Check to see if our REPL button is pressed over 10 seconds
    for i in range(100):
        if repl_button.value() == 0:
            print("Dropping to REPL")
            repl_led.value(1)
            sys.exit()
        utime.sleep_ms(100)

# If we lose connection, repeat this main.py and retry for a connection
print("conexion peredida. Prueba de nuevo.")