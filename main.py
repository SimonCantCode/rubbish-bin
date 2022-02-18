#!/bin/env python3
# Make this execute on boot
from time import sleep
import RPi.GPIO as GPIO
from supersonic import Supersonic # Supersonic uses GPIO.BCM
import requests

# Height is used to compare how full the bin is
rubbish_bin_height = 100

# Function to uppdate the distance on the website
def uppdate(status, distance):
    # Website url and password are located in files hidden with .gitignore
    url = open("url.txt", "r")
    password = open("password.txt", "r")
    _data = {'status': status, 'distance': distance, 'password': password.read().replace('\n', '')}
    requests.post(url.read().replace('\n', ''), data=_data)

#set GPIO Pins
#GPIO_TRIGGER = 18
#GPIO_ECHO = 24
sensor1 = Supersonic(18, 24)

# main
if __name__ == '__main__':
    dist=0
    try:
        while True:
            dist = sensor1.distance()
            if dist < rubbish_bin_height and dist > 0:
                print("Distance to garbage = {} cm".format(dist))
                uppdate(str((dist/rubbish_bin_height)*100) + "%", dist)
                sleep(1)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program shut down by user")
        uppdate("Inactive", dist)
        GPIO.cleanup()
