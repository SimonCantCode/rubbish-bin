#!/bin/env python3
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from supersonic import Supersonic
from stepmotor_wud import Stepmotor
import requests

# Height is used to compare how full the bin is
rubbish_bin_height = 100 # cm
full_distance = 4 # cm

# Function to uppdate the distance on the website
def uppdate(status, distance):
    # Website url and password are located in files hidden with .gitignore
    url = open("url.txt", "r")
    password = open("password.txt", "r")

    _data = {'status': status, 'distance': distance, 'password': password.read().replace("\n", "")}
    x = requests.post(url.read().replace("\n", ""), data=_data)
    return x.text

#set GPIO Pins
#GPIO_TRIGGER, GPIO_ECHO
sensor1 = Supersonic(18, 24)
sensor2 = Supersonic(25, 5)

motor = Stepmotor(22, 17, 27, 4)

# main
if __name__ == '__main__':
    dist=0
    try:
        while True:
            # Distance to garbage meter
            dist = sensor1.distance()
            if dist < rubbish_bin_height and dist > 0:
                print("Distance to garbage = {} cm".format(dist))
                uppdate(str(round((dist/rubbish_bin_height)*100)) + "% \full", round(dist))
                sleep(1)

            # Lid opener sensor
            if sensor2.distance() < 10 and sensor1.distance() > full_distance:
                print("Opening...")
                motor.step(500)
                while sensor2.distance() < 10:
                    sleep(0.5)
                sleep(2)
                print("Closing...")
                motor.step(-500)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program shut down by user")
        uppdate("Inactive", "null")
        GPIO.cleanup()