import RPi.GPIO as GPIO
from time import sleep     

import requests
from datetime import datetime 

GPIO.setmode(GPIO.BCM)  # BCM = numeração GPIO
inA = 16
outA = 18
outB = 11
GPIO.setup(inA, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Entrada inA com pullup (= 1)
GPIO.setup(outA, GPIO.OUT, initial=0)
GPIO.setup(outB, GPIO.OUT)

count=0
auxInput = 1
switchInput = 0

def post(auxInput):
        # configurações do serviço Web (alterar para URL correta)
        paramUrl = 'http://10.42.0.151/api/lab04_api_post_json_switch.php'
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
                GPIO.output(outA, 1)
                post(1)
                GPIO.output(outB, GPIO.HIGH)
                print("botao pressionado", flush=True)
            elif(tempInput == 1):
                GPIO.output(outA, 0)
                post(0)
                GPIO.output(outB, GPIO.LOW)
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

