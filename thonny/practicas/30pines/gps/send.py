import time
import ubinascii
import machine
import network
import requests as requests
import gc
gc.mem_alloc()

ssid = 'Jdvpl'
password = 'R@p1df@5t'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

dat={"temperatura_rpi": 100}
header={"content-type":"application/json"}
link="https://us-central1-pultemsoft.cloudfunctions.net"

r = requests.request("POST",link,data=dat,headers=header)
r.close()
print(r.text)