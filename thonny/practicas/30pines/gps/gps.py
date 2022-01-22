from machine import UART, Pin, I2C
from micropyGPS import MicropyGPS
import utime
import sh1106
import network
import nmea
import network, time, urequests
import json

# el tx debe ir al rx2 y el rx al tx2

WiFi_SSID = "Jdvpl"
WiFi_PASS = "R@p1df@5t"

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = sh1106.SH1106_I2C(oled_width, oled_height, i2c)


def conectaWifi (red, password):
    global miRed
    miRed = network.WLAN(network.STA_IF)     
    if not miRed.isconnected():              #Si no está conectado…
        miRed.active(True)                   #activa la interface
        miRed.connect(red, password)         #Intenta conectar con la red
        print('Conectando a la red', red +"…")
        timeout = time.time ()
        while not miRed.isconnected():           #Mientras no se conecte..
            if (time.ticks_diff (time.time (), timeout) > 10):
                return False
    return True

if conectaWifi ("Jdvpl", "R@p1df@5t"):
    print ("Conexión exitosa!")
    print('Datos de mi red (IP/netmask/gw/DNS):', miRed.ifconfig())
    url = "https://us-central1-pultemsoft.cloudfunctions.net/app/api/users"
    print(url)


    oled.text('JDVPL', 0, 0)  # Afficher les deux mots ''
    oled.text('ESP32', 0, 10)
    oled.show()
    uart = UART(2, 9600)
    now = utime.ticks_ms()
    my_nmea = nmea.nmea(debug=1)

    
    bandera=True

    while 1:
        while uart.any():
            b = uart.read()
            my_nmea.parse(b)

        if utime.ticks_diff(utime.ticks_ms(), now) > 5000:
                now = utime.ticks_ms()
                print('{} {}'.format(my_nmea.latitude, my_nmea.longitude))
                lat = my_nmea.latitude
                lng = my_nmea.longitude

                if lat !=0 and lng !=0 and bandera:
                    payload = {
                    "name": "Juan Daniel",
                    "lat": lat,
                    "lon": lng,
                    "eps": "Sanitas",
                    "cc":"1077870326"
                    }
                    data=(json.dumps(payload)).encode()
                    headers = {
                    'Content-Type': 'application/json'
                    }
                    print(payload)
                    response = urequests.post(url,data)
                    if response.status_code != 200:
                        raise Exception(response.text)
                    bandera=False
                
                oled.fill(0)
                y = 0
                dy = 10
                oled.text("Lat:{}".format(my_nmea.latitude),  0, y)
                y += dy
                oled.text("Lng:{}".format(my_nmea.longitude),  0, y)
                oled.show()
else:
       print ("Imposible conectar")
       miRed.active (False)


# libreria para trabajar con la spi