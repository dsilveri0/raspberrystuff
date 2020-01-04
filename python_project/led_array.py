outA = 18

def initArrayLED():
    GPIO.setup(outA, GPIO.OUT, initial=0)

def setLED0():
    GPIO.output(outA, 1)
