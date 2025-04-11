#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

#Code used to generate 4x5 color sheet at 300DPI
#Generates alternating vertical lines instead of pixel distribution
def main():
    """ Main program """
    #Generate array
    colorArray = np.array([(255,0,0), (0,255,0), (0,0,255)])
    DotArray = np.tile(colorArray, (474,397))#564060
    #print(DotArray)
    #Generate image
    #im = Image.new('RGB', (1190, 1422))
    #im.putdata(DotArray)
    im = Image.fromarray(DotArray, 'RGB').show()
    im.save('testLines.png')
if __name__ == "__main__":
    main()