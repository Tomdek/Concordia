#!/usr/bin/env python
'''
Created on 23 nov. 2016

@author: Thomas
'''
import XLoBorg
import time
import os

#declare variables
SOUND_PATH = "/home/pi/XLoBorg/Concordia/Action_On_Impact/src/" #path to folder containing sound files
soundOne = 'R2D2.wav' #name of sound file
soundTwo = 'R2D2a.wav'
soundThree = 'R2D2b.wav'
soundFour = 'R2D2c.wav'
soundFive = 'R2D2d.wav'
soundSix = 'R2D2e.wav'
interval = 1
thresholdSumLow = .5
thresholdSumHigh = 1.5

#Method: play sound file
def playSound(filename):
    #command = 'bash -c "aplay %s &> /dev/null &"' % (filename)
    command = "aplay " + SOUND_PATH + filename
    os.system(command)
    print("sound file played :mood:yaaaay")

#try:
playSound(soundOne)
playSound(soundTwo)
playSound(soundThree)
playSound(soundFour)
playSound(soundFive)
playSound(soundSix)
    #Loop indefinitely
    #check for changes
        #get sensor data
            #log it
            #if 'hit' detected 
            #play random sound
#Exception KeyboardInterrupt:
#    pass

#Log data 