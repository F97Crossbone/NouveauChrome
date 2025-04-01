#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

#Code used to generate 4x5 color sheet at 300DPI
#Actual measurement of 4x5 film is 3.91x4.9 in (at least Foma 200)
#Actual exposure area is 3.968x4.74
#Exposed picture is approx 1190x1422 at 300DPI
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
    im.save('test.png')
if __name__ == "__main__":
    main()