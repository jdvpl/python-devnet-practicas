from hcsr04 import HCSR04
from machine import Pin,I2C
from sh1106 import SH1106_I2C
import network, time, urequests
import framebuf


ancho=128
alto=64


# pines
# pin d5  es el de echo hcsr04
# pin d18 es el de triger hcsr04
i2c=I2C(0,scl=Pin(22),sda=Pin(21))
oled =SH1106_I2C(ancho, alto, i2c)

sensor = HCSR04(trigger_pin=5, echo_pin=18,echo_timeout_us=1000000)

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


def buscar_icono(ruta):
    dibujo= open(ruta, "rb")  # Abrir en modo lectura de bist
    dibujo.readline() # metodo para ubicarse en la primera linea de los bist
    xy = dibujo.readline() # ubicarnos en la segunda linea
    x = int(xy.split()[0])  # split  devuelve una lista de los elementos de la variable solo 2 elemetos
    y = int(xy.split()[1])
    icono = bytearray(dibujo.read())  # guardar en matriz de bites
    dibujo.close()
    return framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)


if conectaWifi ("Jdvpl", "R@p1df@5t"):
    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    url = "https://maker.ifttt.com/trigger/telegram_distance_controller/with/key/cYDCD02FxQbe-weUclU0OpIc6yi5MfmT5bOdPLt6LO3?"  

    while True:
        distance = sensor.distance_cm()
        distancia="{:.2f}cm ".format(distance)
        distanciaM=distance/100
        distanceKm=distanciaM/1000;
        print(distancia)
        time.sleep(1)
        oled.fill(0)
        oled.blit(buscar_icono("imagenes/python.pbm"), 0, 0)  
        oled.text(f"{distancia}",60,20)
        oled.show()
        if distance <15:
            oled.fill(0)
            oled.blit(buscar_icono("imagenes/alerta.pbm"), 0, 0)  
            oled.text(f"{distancia}",60,20)
            oled.show()
            respuesta = urequests.get(url+"&value1="+str(distance)+"cm&value2="+str(distanciaM)+"mts&value3="+str(distanceKm)+"km")
            print(respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
    
else:
       print ("Imposible conectar")
       miRed.active (False)








