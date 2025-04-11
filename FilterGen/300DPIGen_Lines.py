#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

#Code used to generate 4x5 color sheet at 300DPI
#Generates alternating vertical lines instead of pixel distribution
def main():
    """ Main program """
    #Generate array
    img_w = 1422 #width
    img_h = 1190 #height
    LineArray = np.zeros((img_h, img_w, 3), dtype=np.uint8) #create empty array for color matrix
    j = 0 # initialize index
    for i in range(img_h):
        if j == 3: #restart index
            j = 0
        match j: # alternate color for rows
            case 0:
                color = (250,0,0)
            case 1:
                color = (0,250,0)
            case 2:
                color = (0,0,250)
        LineArray[i] = color #set row to color
        j += 1 #step index
    #print(LineArray) #display resulting array
    #Add orientation markers
    mark_w = 25
    mark_h = 100
    mark = np.zeros((mark_h, mark_w, 3), dtype=np.uint8)
    LineArray[0:mark_h, 0:mark_w] = mark
    #Generate image
    im = Image.fromarray(LineArray, 'RGB')#.show() #turn to RGB image
    im.save('testLines.png')
if __name__ == "__main__":
    main()