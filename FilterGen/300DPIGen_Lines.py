#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

#Code used to generate 4x5 color sheet at 300DPI
#Generates alternating vertical lines instead of pixel distribution
def main():
    """ Main program """
    #Generate array
    #colorArray = np.array([(255,0,0), (0,255,0), (0,0,255)])
    img_w = 474
    img_h = 397
    LineArray = np.zeros((img_h, img_w, 3), dtype=np.uint8)
    print(LineArray.shape)
    j = 0
    for i in range(397):
        print(i)
        if j == 3:
            j = 0
        match j:
            case 0:
                color = (250,0,0)
            case 1:
                color = (0,250,0)
            case 2:
                color = (0,0,250)
        print(color)
        LineArray[i] = color
        j += 1
    print(LineArray)
    #Generate image
    im = Image.fromarray(LineArray, 'RGB').show()
    #im.save('testLines.png')
if __name__ == "__main__":
    main()