import RPi.GPIO as GPIO

leds = [18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

def initArrayLED():
    for led in leds:
        GPIO.setup(led, GPIO.OUT, initial=0)

def setAllLedsHigh():
    for led in leds:
        GPIO.output(led, 1)
    
def setAllLedsLow():
    for led in leds:
        GPIO.output(led, 0)

def setLEDHigh(num):
    GPIO.output(leds[num], 1)


def setLEDLow(num):
    GPIO.output(leds[num], 0)

def variableRangeLED(num):
    setAllLedsLow()
    for i in range(0, num+1):
        setLEDHigh(num)
