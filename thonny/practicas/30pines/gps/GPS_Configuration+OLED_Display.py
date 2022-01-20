from machine import UART, Pin, SPI,I2C
from micropyGPS import MicropyGPS
import utime
import sh1106
import network
import nmea



# el tx debe ir al rx2 y el rx al tx2

WiFi_SSID = "Jdvpl"
WiFi_PASS = "R@p1df@5t"

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = sh1106.SH1106_I2C(oled_width, oled_height, i2c)



oled.text('JDVPL', 0, 0)  # Afficher les deux mots ''
oled.text('ESP32', 0, 10)
oled.show()
uart = UART(2, 9600)
now = utime.ticks_ms()
my_nmea = nmea.nmea(debug=1)

while 1:
	while uart.any():
		b = uart.read()
		my_nmea.parse(b)

	if utime.ticks_diff(utime.ticks_ms(), now) > 5000:
            now = utime.ticks_ms()
            print('{} {}'.format(my_nmea.latitude, my_nmea.longitude))
            lat = my_nmea.latitude
            lng = my_nmea.longitude
            
            oled.fill(0)
            y = 0
            dy = 10
            oled.text("Latitud:{}".format(my_nmea.latitude),  0, y)
            y += dy
            oled.text("Longitud:{}".format(my_nmea.longitude),  0, y)
            oled.show()
