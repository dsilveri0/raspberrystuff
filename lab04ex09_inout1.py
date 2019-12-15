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
try:  
	print("CTRL+C para terminar.")
	while True:
		tempInput = GPIO.input(inA)
		
		if(tempInput == 0):
			if (auxInput == 0):
				auxInput = 1
			else:
				auxInput = 0
			GPIO.output(outA, auxInput)
			print("swith =",auxInput,",", end="", flush=True) #sem \n e com flush
			count=count
			#print("  Contator = ",count)
			sleep(0.2)
			print("\nPressione o Switch ou as teclas CTRL+C para terminar.")
except KeyboardInterrupt:
	print("\nPrograma terminado pelo utilizador.")		
except:
	print("\nErro!!!")
finally:
	print("A fazer 'reset' ao GPIO...", end="")
	GPIO.cleanup()
	print("ok.")
print("Fim do programa.")

