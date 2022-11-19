# pico-wireless
code to connect Pico W to wireless 

Original Raspberry Pi Foundation Documentation - https://forums.raspberrypi.com/viewtopic.php?t=332130

wireless.py enables your Pico W to connect to the internet.  

Remember to update the following values to suit:

    ssid = 'Enter Your SSID'
    password = 'enter your LAN password'
    
    
Added a few extras to make your Pico W blink 3 times when your device is connected to the internet: 

else:
    s = 3
    while s > 0:
        s -= 1
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)


When connected, the following print string will output your SSID and IP Address (see example output below): 

    status = wlan.ifconfig()
    print( 'Connected to ' + ssid + '. ' + 'Device IP: ' + status[0] )
    
Example output: Connected to FBI Van. Device IP: 192.168.X.XXX



    
