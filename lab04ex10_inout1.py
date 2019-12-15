import RPi.GPIO as GPIO
from time import sleep     

import requests
from datetime import datetime 

GPIO.setmode(GPIO.BCM)  # BCM = numeração GPIO
inA = 16
outA = 18
GPIO.setup(inA, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Entrada inA com pullup (= 1)
GPIO.setup(outA, GPIO.OUT, initial=0)

count=0
auxInput = 1
switchInput = 0
try:
    sleep(0.2)
    print("CTRL+C para terminar.")
    tempInput = GPIO.input(inA)
    switchInput = tempInput
    while True:
        tempInput = GPIO.input(inA)
        
        if(switchInput != tempInput):
            if(tempInput == 0):
                GPIO.output(outA, 1)
                print("botao pressionado", flush=True)
            elif(tempInput == 1):
                GPIO.output(outA, 0)
                print("botao nao pressionado", flush=True)
            switchInput = tempInput
        switchInput = tempInput

except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")		
except:
    print("\nErro!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")

