import time
import network
from machine import Pin

led = Pin("LED", Pin.OUT)
led.value(1) # LED On
led.value(0) # LED Off



ssid = 'Enter Your SSID'
password = 'enter your LAN password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    s = 3
    while s > 0:
        s -= 1
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
        
    #print('connected')
    status = wlan.ifconfig()
    print( 'Connected to ' + ssid + '. ' + 'Device IP: ' + status[0] )