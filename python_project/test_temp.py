import RPi.GPIO as GPIO
from time import sleep
import requests
from datetime import datetime

from led_array_module import *
from temp_lumi_module import *
from motor_control_module import *

GPIO.setmode(GPIO.BCM)

initArrayLED()
initMotor()

def luminosityDisplayControl():
    percent = getLumPercentage()
    print(percent)
    updateProgressBar(round(percent/10))        

try:
    sleep(0.2)
    print("Control+C para terminar.")

    while True:
        sleep(1)
        print("Temperature: ", getTempVoltage())        
        print("Luminosidade: ", getLumPercentage())

except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")
except:
    print("\nError!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")
