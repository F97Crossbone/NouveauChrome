#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

#Code used to generate 4x5 color sheet at 300DPI
#Generates alternating vertical lines instead of pixel distribution
def main():
    """ Main program """
    #Generate array
    img_w = 1470 #width
    img_h = 1175 #height
    LineArray = np.zeros((img_h, img_w, 4), dtype=np.uint8) #create empty array for color matrix
    j = 0 # initialize index
    for i in range(img_h):
        if j == 3: #restart index
            j = 0
        match j: # alternate color for rows
            case 0:
                color = (250,0,0,255)
            case 1:
                color = (0,250,0,255)
            case 2:
                color = (0,0,250,255)
        LineArray[i] = color #set row to color
        j += 1 #step index
    #print(LineArray) #display resulting array
    #Add orientation markers
    mark_w = 200
    mark_h = 25
    mark = np.zeros((mark_h, mark_w, 4), dtype=np.uint8)
    LineArray[0:mark_h, 0:mark_w] = mark
    #Generate image
    im = Image.fromarray(LineArray, 'RGBA')#.show() #turn to RGB image
    im.save('testLines.png')
    #Print paper generator
    A4_h = 2480
    A4_w = 3508
    A4Array = np.zeros((A4_h, A4_w, 4), dtype=np.uint8)
    A4Array[40:img_h+40, 40:img_w+40] = LineArray
    A4Array[img_h+100:(2*img_h)+100, 40:img_w+40] = LineArray
    A4Array[40:img_h+40, img_w+200:(2*img_w)+200] = LineArray
    A4Array[img_h+100:(2*img_h)+100, img_w+200:(2*img_w)+200] = LineArray
    im = Image.fromarray(A4Array, 'RGBA')#.show() #turn to RGB image
    im.save('testLines_Print.png')
if __name__ == "__main__":
    main()