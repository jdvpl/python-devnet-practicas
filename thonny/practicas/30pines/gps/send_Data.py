import network, time
import urequests as requests
import json

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
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    # envia data
    url = "http://us-central1-pultemsoft.cloudfunctions.net/app/api/users"
    data = {
    "name":"Daniel",
    "lat":9.6676,
    "lon":-74.5618,
    "eps":"26132132lol"
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(url,data=json.dumps(data),headers=headers)
    print(r.json())

    while True:
        distancia = 5
        print(distancia)
        time.sleep(1)
else:
       print ("Imposible conectar")
       miRed.active (False)








