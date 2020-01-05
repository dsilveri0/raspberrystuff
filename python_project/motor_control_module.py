import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pwmPort = 13
controlDir0 = 19
controlDir1 = 26

GPIO.setup(pwmPort, GPIO.OUT)
pwm = GPIO.PWM(pwmPort, 100)

def initMotor():
    GPIO.setup(controlDir0, GPIO.OUT, initial=0)
    GPIO.setup(controlDir1, GPIO.OUT, initial=0)

    pwm.start(0)

def changeSpeedMotor(dutyCycle):
    GPIO.output(controlDir0, 0)
    GPIO.output(controlDir1, 1)
    pwm.ChangeDutyCycle(dutyCycle)

def stopMotor():
    GPIO.output(controlDir0, 0)
    GPIO.output(controlDir1, 0)
    pwm.ChangeDutyCycle(0)
