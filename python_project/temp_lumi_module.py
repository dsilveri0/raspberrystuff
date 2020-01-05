import RPi.GPIO as GPIO
import smbus
import math
from time import sleep

address = 0x48
bus = smbus.SMBus(1)
lumSensor = 0x40
tempSensor = 0x43

def getSensorRawData(sensor):
    bus.write_byte(address,sensor)
    value = 0
    for i in range(0, 299):
        sleep(0.001)
        value += bus.read_byte(address)
    return value/300

def getLumPercentage():
    rawValue = getSensorRawData(lumSensor)
    print("lum ", round(rawValue/2.5, 0))
    return round(rawValue/2.5, 0)

def getTempVoltage():
    rawValue = getSensorRawData(tempSensor)
    voltage = rawValue / 255 * 3.3
    rT = 10 * voltage / (3.3 - voltage)
    kelvin = 1/(1/(273.15 + 25) + math.log(rT/10)/3950.0)
    celcius = kelvin - 273.15
    print("temp ", round(celcius-4, 1))
    return round(celcius-4, 1)
