import RPi.GPIO as GPIO
from time import sleep
import requests
from datetime import datetime

from led_array import *

GPIO.setmode(GPIO.BCM)

initArrayLED()

try:
    sleep(0.2)
    print("Control+C para terminar.")

    while True:
        #for i in range(0, 10):
        sleep(1)
        variableRangeLED(0)

        sleep(1)
        variableRangeLED(2)

        sleep(1)
        variableRangeLED(4)

        sleep(1)
        variableRangeLED(6)

        sleep(1)
        variableRangeLED(8)

except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")
except:
    print("\nError!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")
