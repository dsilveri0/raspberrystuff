import RPi.GPIO as GPIO
import smbus
from time import sleep

address = 0x48
bus = smbus.SMBus(1)
lumSensor = 0x40

def getSensorRawData(sensor):
    bus.write_byte(address,lumSensor)
    bus.read_byte(address)
    value = bus.read_byte(address)

    return value

def getLumPercentage():
    rawValue = getSensorRawData(lumSensor)
    return rawvalue/2.5
