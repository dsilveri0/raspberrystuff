import RPi.GPIO as GPIO
import dht11
import time
import datetime

#initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#read data using pin 24, previous was 14
instance = dhtll.DHTll(pin=24)

while True:
    result=instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.Temperature)
        print("Humidity: %d %%" % result.humidity)

    time.sleep(1)
