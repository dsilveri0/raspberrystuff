import RPi.GPIO as GPIO

led0 = 14
led1 = 15
led2 = 18
led3 = 23
led4 = 24
led5 = 25
led6 = 12
led7 = 16
led8 = 20
led9 = 21

def initArrayLED():
    GPIO.setup(led0, GPIO.OUT, initial=0)

def setAllLEDS():
    for i in range(9, 5, -1)
        name = "led{}".format(i)
        GPIO.output(name, 1)

def setLED0():
    GPIO.output(led0, 1)
