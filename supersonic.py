import RPi.GPIO as GPIO
from time import sleep
from time import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

class Supersonic:
    def __init__(self, GPIO_TRIGGER, GPIO_ECHO):
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
 
    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
    
        # set Trigger after 0.01ms to LOW
        sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
    
        StartTime = time()
        StopTime = time()
    
        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time()
    
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    
        # returns the distance in cm
        return distance