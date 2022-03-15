#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

class Stepmotor:
    def __init__(self, out1, out2, out3, out4):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4

        GPIO.setup( out1, GPIO.OUT )
        GPIO.setup( out2, GPIO.OUT )
        GPIO.setup( out3, GPIO.OUT )
        GPIO.setup( out4, GPIO.OUT )

        GPIO.output( out1, GPIO.LOW )
        GPIO.output( out2, GPIO.LOW )
        GPIO.output( out3, GPIO.LOW )
        GPIO.output( out4, GPIO.LOW )

    # the meat
    def step(self, step_count):
        i = 0
        for i in range(step_count):
            if i%4==0:
                GPIO.output( self.out4, GPIO.HIGH )
                GPIO.output( self.out3, GPIO.LOW )
                GPIO.output( self.out2, GPIO.LOW )
                GPIO.output( self.out1, GPIO.LOW )

            elif i%4==1:
                GPIO.output( self.out4, GPIO.LOW )
                GPIO.output( self.out3, GPIO.LOW )
                GPIO.output( self.out2, GPIO.HIGH )
                GPIO.output( self.out1, GPIO.LOW )

            elif i%4==2:
                GPIO.output( self.out4, GPIO.LOW )
                GPIO.output( self.out3, GPIO.HIGH )
                GPIO.output( self.out2, GPIO.LOW )
                GPIO.output( self.out1, GPIO.LOW )

            elif i%4==3:
                GPIO.output( self.out4, GPIO.LOW )
                GPIO.output( self.out3, GPIO.LOW )
                GPIO.output( self.out2, GPIO.LOW )
                GPIO.output( self.out1, GPIO.HIGH )

            time.sleep( step_sleep )