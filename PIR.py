#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:51:47 2019

@author: daniel
"""

import ASUS.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)


PirSensor   = 257
#TouchSensor = 256

GPIO.setup(PirSensor,GPIO.IN)

try:
    while True:
        if(GPIO.input(PirSensor)):
            print ("***** pir sensor activated *****")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()