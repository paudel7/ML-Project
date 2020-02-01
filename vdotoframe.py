# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:47:08 2020

@author: paude
"""
import cv2
import numpy as np
import os

# Playing video from file:
vdo = cv2.VideoCapture('video_20200130.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = vdo.read()

    # Saves image of the current frame in jpg file
    name = './videotoframe/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
vdo.release()
cv2.destroyAllWindows()