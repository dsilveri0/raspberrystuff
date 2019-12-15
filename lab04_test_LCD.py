import RPi.GPIO as GPIO
from time import sleep     

import requests
from datetime import datetime 

GPIO.setmode(GPIO.BCM)  # BCM = numeração GPIO
inA = 16
outA = 18
outB = 11
outControlDir = 2 #controla direcao PIN 1A
outControlDir2 = 3 #controla direcao PIN 2A
outPWM = 4 #ativa o motor

GPIO.setup(inA, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Entrada inA com pullup (= 1)
GPIO.setup(outA, GPIO.OUT, initial=0)
GPIO.setup(outB, GPIO.OUT)

GPIO.setup(outControlDir, GPIO.OUT)
GPIO.setup(outControlDir2, GPIO.OUT)

GPIO.setup(outPWM, GPIO.OUT)

GPIO.output(outControlDir, GPIO.LOW)
GPIO.output(outControlDir2, GPIO.LOW)

pwm=GPIO.PWM(outPWM, 100)
pwm.start(0)

count=0
auxInput = 1
switchInput = 0

GPIO.output(outControlDir, GPIO.HIGH)
GPIO.output(outControlDir2, GPIO.LOW)

def post(auxInput):
        # configurações do serviço Web (alterar para URL correta)
        paramUrl = 'http://192.168.1.92/api/lab04_api_post_json_switch.php'
        paramAuth = 'irsotesppsi'
        paramKey = 'switch'
        paramNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        paramJSON = {'auth':paramAuth, 'key':paramKey, 'value':auxInput, 'date':paramNow}
        paramHeaders = {'content-type': 'application/json'}
        # enviar dados para o serviço Web (formato: json)
        print("a enviar para o serviço Web...")
        r = requests.post(paramUrl, json=paramJSON, headers=paramHeaders)
        # mostrar resultados
        print(r)
        print(r.text)
        #print("Fim do programa.")
        return;

try:

    sleep(0.2)
    print("CTRL+C para terminar.")
    tempInput = GPIO.input(inA)
    switchInput = tempInput

    while True:
        tempInput = GPIO.input(inA)

        if(switchInput != tempInput):
            if(tempInput == 0):
                #post(1)
                GPIO.output(outA, 1)
                GPIO.output(outB, GPIO.HIGH)
                pwm.ChangeDutyCycle(25)
                GPIO.output(outControlDir, GPIO.LOW)
                GPIO.output(outControlDir2, GPIO.LOW)
                GPIO.output(outControlDir, GPIO.HIGH)
                GPIO.output(outControlDir2, GPIO.LOW)
                #GPIO.output(outPWM, 1)
                print("botao pressionado", flush=True)

            elif(tempInput == 1):
                #post(0)
                GPIO.output(outA, 0)
                GPIO.output(outB, GPIO.LOW)
                pwm.ChangeDutyCycle(25)
                GPIO.output(outControlDir, GPIO.LOW)
                GPIO.output(outControlDir2, GPIO.LOW)
                GPIO.output(outControlDir, GPIO.LOW)
                GPIO.output(outControlDir2, GPIO.HIGH)
                #GPIO.output(outPWM, 0)
                print("botao nao pressionado", flush=True)

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

