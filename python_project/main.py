import RPi.GPIO as GPIO
from time import sleep
import requests
from datetime import datetime

from led_array_module import *
from temp_lumi_module import *

GPIO.setmode(GPIO.BCM)

initArrayLED()

try:
    sleep(0.2)
    print("Control+C para terminar.")

    while True:
       sleep(1)
       print(getLumPercentage())



        # for i in range(0, 10):
        #    sleep(1)
        #    updateProgressBar(i)

except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")
except:
    print("\nError!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")
