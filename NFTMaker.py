from distutils.log import error
from random import randint
from wand.image import Image
import os
import sys


'''
Author: Vijeet Yarlagadda, vijeetyarla@gmail.com
Usage: To use this script, you require the following dependencies:
        - ImageMagick
        - the Wand library for Python (a Python binding for ImageMagick)
        - Python 3.x
    FLAGS:
        - -n Number of images to create
        - -b designate base layer
Folder Structure: store all layers in separate folders within the same
                  directory that this script is located in: (follow the same naming conventions)
                  - root
                      - NFTMaker.py
                      - base
                          - base_1.png
                          - base_2.png
                      - layer1
                          - layer1_1.png
                          - ...
Examples: NFTMaker.py -b ./base -n 10000 
'''
def help():
    print('''Usage: To use this script, you require the following dependencies:
        - ImageMagick
        - the Wand library for Python (a Python binding for ImageMagick)
        - Python 3.x
    FLAGS:
        - -n Number of images to create
        - -b designate base layer
Folder Structure: store all layers in separate folders within the same
                  directory that this script is located in: (follow the same naming conventions)
                  - root
                      - NFTMaker.py
                      - base
                          - base_1.png
                          - base_2.png
                      - layer1
                          - layer1_1.png
                          - ...
Examples: NFTMaker.py -b ./base -n 10000 ''')


#Analyzing arguments given
args = list(sys.argv)
dirs = [name for name in os.listdir(".") if os.path.isdir(name)]
if "output" not in dirs:
    os.mkdir("output")

exclude = ['git', '__pycache__', 'output'] #add all folders to exclude to this list

dirs = [name for name in dirs if "layer" in name and name not in exclude] 

if '-h' in args or '--help' in args:
    help()
if '-n' not in args:
    help()
    error("You must use the flag -n to set the number of images you want to create")
    quit()
else:
    n = int(args[args.index('-n') + 1])
if '-b' not in args:
    help()
    error("You must use the flag -b to set the base image folder")
    quit()
else:
    base = str(args[args.index('-b') + 1])

#splitting layers and base
layers = dirs.copy()
layers.remove(base)

#get base images and layer images
base_images = list(os.listdir('./' + base))
layer_images = {}
for layer in layers:
    layer_images[layer] = list(os.listdir('./' + layer))

#composite images to create n different randomly generated images

for i in range(n):
    with Image(filename=base + '/' + base_images[randint(0, len(base_images) - 1)]) as b:
        for layer in layers:
            with Image(filename=layer + '/' + layer_images[layer][randint(0, len(layer_images[layer]) - 1)]) as l:
                b.composite(l, left=0, top=0)
                b.save(filename = './output/' + str(i) + ".png")
        print("created " +  './output/' + str(i) + ".png")


