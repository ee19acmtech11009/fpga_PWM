import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

GPIO.setup(26, GPIO.OUT)

GPIO.output(12,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(36,GPIO.LOW)

GPIO.output(26,GPIO.LOW)



