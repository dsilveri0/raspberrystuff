#!/usr/bin/env python3

import smbus
import time

address = 0x48	# default address of PCF8591
bus=smbus.SMBus(1)
cmdActive=0x40	# command, 0100 0000

#a0 = 64
#a1 = 65

#cmdDeactive=0x60

def getTemperatureRaw(chn): # read ADC value,chn:0,1,2,3
        #value = bus.read_byte_data(address,cmd+chn)
        #value = bus.read_byte_data(address,a1)
        #bus.read_byte_data(address, cmdDeactive+chn)
        bus.write_byte(address,cmdActive+chn)
        #bus.read_byte(address)
        time.sleep(0.2)
        value = bus.read_byte(address)
        return value


def getLuminosityRaw(chn): # read ADC value,chn:0,1,2,3
        #value = bus.read_byte_data(address,cmd+chn)
        #value = bus.read_byte_data(address,a0)
        #bus.read_byte_data(address, cmdDeactive+chn) 
        #bus.write_byte(address,cmdActive+chn)
        bus.write_byte(address,0x40)
        #bus.read_byte(address)
        value = bus.read_byte(address)
        #while value < 2:
        #value = bus.read_byte(address)
        bus.write_byte(address,cmdActive+chn)
        value = bus.read_byte(address)
        #while value > 2:
        #value = bus.read_byte(address)
       
        return value

def analogWrite(value): # write DAC value
	bus.write_byte_data(address,cmdActive,value)

def loop():
        while True:
                luminosity = getLuminosityRaw(0) # read the ADC value of channel 0
                #temperature = getLuminosityRaw(3) # read the ADC value of channel 3
                #analogWrite(luminosity)
                voltageLumi = luminosity / 255.0 * 3.3  # calculate the voltage value
                
                #temperature = getTemperatureRaw(2) # read the ADC value of channel 3
                #luminosity = getLuminosityRaw(0) # read the ADC value of channel 0
                #analogWrite(temperature)
                #voltageTemp = temperature / 255.0 * 3.3  # calculate the voltage value
                
                print ('LUMINOSIDADE : %d, Voltage : %.2f'%(luminosity,voltageLumi))
                #print ('TEMPERATURA : %d, Voltage : %.2f'%(temperature,voltageTemp))
                time.sleep(1.5)

def destroy():
        bus.close()

if __name__ == '__main__':   # Program entrance
        print ('Program is starting ... ')
        try:
            loop()
        except KeyboardInterrupt: # Press ctrl-c to end the program.
            destroy()
