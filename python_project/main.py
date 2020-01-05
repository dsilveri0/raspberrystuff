import RPi.GPIO as GPIO
from time import sleep
import requests
from datetime import datetime

from led_array_module import *
from temp_lumi_module import *
from motor_control_module import *
from post_data_module import *

GPIO.setmode(GPIO.BCM)

initArrayLED()
initMotor()

def luminosityDisplayControl():
    percent = getLumPercentage()
    print(percent)
    updateProgressBar(round(percent/10))        
    
def temperatureMotorControl():
    triggerTemp = 17
    pwmInitial = 25
    
    # Equação da reta Y = PWM, X = Temperatura, tal que y = mx +b
    m = pwmInitial / triggerTemp
    b = pwmInitial - (m * triggerTemp)

    currentTemp = getTempVoltage()
    
    dutyCycle = m * currentTemp + b

    post(currentTemp)    

    print("dutycycle", dutyCycle)
    if (dutyCycle >= pwmInitial):
        changeSpeedMotor(dutyCycle)
    else: 
        stopMotor()

try:
    sleep(0.2)
    print("Control+C para terminar.")

    while True:
        luminosity = luminosityDisplayControl()
        temperature = temperatureMotorControl()


except KeyboardInterrupt:
    print("\nPrograma terminado pelo utilizador.")
except:
    print("\nError!!!")
finally:
    print("A fazer 'reset' ao GPIO...", end="")
    GPIO.cleanup()
    print("ok.")
print("Fim do programa.")
