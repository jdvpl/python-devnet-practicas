import network, time, urequests,I2C
from dht import DHT11
from machine import Pin
from sh1106 import SH1106_I2C

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

sensorDHT = DHT11 (Pin(5))

if conectaWifi ("Jdvpl", "R@p1df@5t"):
    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    url = "https://api.thingspeak.com/update?api_key=UL09TM00U7K3UYYJ"  
    while (True):
        time.sleep (4)
        sensorDHT.measure ()
        temp=sensorDHT.temperature ()
        hum=sensorDHT.humidity()
        print ("T={:02d} ºC, H={:02d} %".format (temp,hum))
        respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum))
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
else:
       print ("Imposible conectar")
       miRed.active (False)