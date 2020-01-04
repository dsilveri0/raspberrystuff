import RPi.GPIO as GPIO
from time import sleep

import requests
from datetime import datetime

GPIO.setmode(GPIO.BCM)

outA = 18

GPIO.setup(outA, GPIO.OUT, initial=0)

try:
    sleep(0.2)
    print("Control+C para terminar.")

    while True:
        GPIO.output(outA, 1)

except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")
except:
    print("\nError!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")
