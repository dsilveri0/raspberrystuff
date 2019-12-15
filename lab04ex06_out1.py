import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) 	# BCM = numeração GPIO

outA = 18
GPIO.setup(outA, GPIO.OUT, initial=0)
tempo = 1
try:
    print("CTRL+C para terminar")
    while True:
        GPIO.output(outA, 1)
        print("GPIO", outA, ": ON")
        sleep(tempo)
        GPIO.output(outA, 0)
        print("GPIO %d : %s" % (outA, "OFF"))   #com formatação
        sleep(tempo)
        tempo+=1
except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")		
except:
    print("\nErro!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")
