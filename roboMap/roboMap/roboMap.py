#!/usr/bin/env python
#-----------------------------------------------------------------------
#		SLAM mapping in Python v0.1
# 		iMapping component using SLAM methods for robotic localisation
#		started: 06/02/2020
#		Comp tested: 
#		Author: AH
#-----------------------------------------------------------------------
import random as rand
import cv2 as cv
import numpy as np
#-----------------------------------------------------------------------
#		Random Map Generator v0.2
# 		marching squares with gaussian smoothing and biarisation
#       in: 
#           intHeight, integer height of map
#           intWidth, integer width of map
#           flDensity, float between 0, 100%
#           boolSmooth, use gaussian smoothing
#		started: 06/02/2020
#		Comp tested: 
#		Author: AH
#-----------------------------------------------------------------------
def MapGenerator(intHeight, intWidth, flDensity, boolSmooth = True):

    arryMap = np.zeros([5,5])
    arryMap = cv.resize(arryMap, (intWidth, intHeight))
    
    for intCountX in range(0, intWidth):
        for intCountY in range(0, intHeight):

            if rand.randint(0, 101) <= flDensity:
                arryMap[intCountX, intCountY] = 255
            else: 
                arryMap[intCountX, intCountY] = 0

    if boolSmooth == True:
        #arryMap = cv.bilateralFilter(arryMap, 3, 2, 2)
        arryMap = cv.GaussianBlur(arryMap, (3,3), 2)

        for intCountX in range(0, intWidth):
            for intCountY in range(0, intHeight):

                if  arryMap[intCountX, intCountY] <= np.mean(arryMap):
                    arryMap[intCountX, intCountY] = 0
                else: 
                    arryMap[intCountX, intCountY] = 1

    return arryMap

#-----------------------------------------------------------------------
#		SLAM mapping in Python v0.1
# 		project Main filder
#		started: 06/02/2020
#		Comp tested: 
#		Author: AH
#-----------------------------------------------------------------------

map = MapGenerator(100, 100, 10)
cv.imshow("", map)
cv.waitKey(1)