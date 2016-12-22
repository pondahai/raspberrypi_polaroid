from __future__ import print_function
import os,time,Image,sys
sys.path.append("/home/pi/Python-Thermal-Printer")
from Adafruit_Thermal import *

import RPi.GPIO as GPIO

photoResize = 512,384

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
while True:
    input_value = GPIO.input(12)
    if input_value == False:
        print("pressed")
	os.system("sudo raspistill --timeout 1 -w 1920 -h 1440 -o temp.jpg")
        Image.open("temp.jpg").resize(photoResize,Image.ANTIALIAS).save("thumbnail.jpg")
        printer.printImage(Image.open("thumbnail.jpg"), True)
        printer.feed(3)
        while input_value == False:
            input_value = GPIO.input(12)
