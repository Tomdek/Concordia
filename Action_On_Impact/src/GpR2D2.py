#!/usr/bin/env python
'''
Created on 23 nov. 2016

@author: Thomas
'''
import XLoBorg
import time
import os

#declare variables
soundOne = 'R2D2.wav'
interval = 1
thresholdSumLow = .5
thresholdSumHigh = 1.5

#Method: play soundfile
def playSound(filename):
    #command = 'bash -c "aplay %s &> /dev/null &"' % (filename)
    command = "aplay ./" + filename
    os.system(command)
    print("soundfile played :mood:hopeful")

#try:
playSound(soundOne)
    #Loop indefinitely
    #check for changes
        #get sensor data
            #log it
            #if 'hit' detected 
            #play random sound
#Exception KeyboardInterrupt:
#    pass

#Log data 