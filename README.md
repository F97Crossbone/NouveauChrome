# NouveauChrome
Repo for the NouveauChrome project, which seeks to modernize the AutoChrome process

# What is AutoChrome?
AutoChrome is an early color photography process that utilized colored starch particles to create a color film mask. When the black and white film was reverse processed and was backlit a color image would appear. Autochrome is what is known as a screen process, in which a colored screen of some form is placed in front of a panchromatic B&W emulsion. A general overview of these processes can be found [Here](https://filmcolors.org/cat/screen-processes/), but there are several process that are of interest in addition to AutoChrome. Most commercial screen processes did not use the randomized pattern produced by dyed starch, but rather alternating squares, circles, or lines of a color. These processes, such as the Paget or McDonough, more closely resemble what the final NouveauChrome photo will look like.

# Why update the process?
AutoChrome is an incredibly complicated process to perform at home. While specific details can be found at [John Hilty's](https://www.jonhilty.com/screenplateguide) exhaustive guide, the gist of the process was:

1. Sort starch particles to get a consistent small size
2. Dye the starch particle orange, green, and violet
3. Mix the dyed starch particles
4. Affix the starch to a glass plate using a clear varnish
5. Coat the back of the starch with a different varnish
6. Apply a film emulsion to the back of the second varnish
7. Take a picture
8. Reverse process the image

While the resulting images are beautiful, they are also light sensitive and tend to degrade over time. 

# How does NouveauChrome change the process?
The main challenges associated with the AutoChrome process are the creation of the color mask and the following emulsion (so essentially, the whole process). The NouveauChrome project seeks to solve these issues by

1. Using modern transparency printing techniques to digitally print color masks
2. Using off the shelf B&W 4x5 film as the emulsion

# Process concept

1. Using the python script, an image for transparency printing is generated
    * Ideally four masks per A4 transparency sheets, at 600+DPI
2. Load a standard 4x5 film holder with standard B&W film, and then load the color mask on top
    * The mask will have orientation markings on it so that the orientation of the mask with respect to the film at the time of shooting is known 
3. Reverse process the film separately from the mask
    * Details of the exact process will be shared when results are satisfying, but a standard reversal process should suffice
    * [Current planned process](https://imager.ie/a-better-peroxide-black-and-white-reversal-bleach/)
4. Adhere the color mask to the developed film using the orientation marks

The resulting piece should resemble an AutoChrome

# Potential Challenges
1. Reversal processing
2. Color mask adhesion
3. Color mask orientation
4. Color mask generation
    * Ultimately this mask will be digitally generated, and may result in a "pixelated" look
5. Color mask balance
    * The color balance of the final image may not be accurate in the initial round of testing, as the standard RGB color separation is used. Panchromatic film does not have an even sensitivity towards all light wavelengths, so adjustments in the values of each color may need to be done

# Current Status
* Initial code for generating color masks (both individual pixels and alternating lines) is completed, and available in the FilterGen directory. Commercial printers have been contacted regarding the feasibility of printing the current designs
