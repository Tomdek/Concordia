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
NUMBER_OF_SOUNDS = 6 #numer of sound files, number used for RNG
soundOne = 'R2D2.wav' #name of sound file add as many as you specify in NUMBER_OF_SOUNDS
soundTwo = 'R2D2a.wav'
soundThree = 'R2D2b.wav'
soundFour = 'R2D2c.wav'
soundFive = 'R2D2d.wav'
soundSix = 'R2D2e.wav'
interval = 1
thresholdSumLow = .5
thresholdSumHigh = 1.5

xl = XLoBorg
xl.init()

#Method: play sound file
def playSound(filename):
    #command = 'bash -c "aplay %s &> /dev/null &"' % (filename)
    command = "aplay " + SOUND_PATH + filename
    os.system(command)
    print("sound file played :mood:yaaaay")

#Loop indefinitely
try:
    x, y, z = xl.ReadAccelerometer()
    moveSum = x + y + z
    print(moveSum)
    
    if thresholdSumLow <= moveSum <= thresholdSumHigh:
        playSound(soundOne)
        print("movement within threshold")        

            #log it
            #play random sound
except KeyboardInterrupt:
    pass

#Log data 