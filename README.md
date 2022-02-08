# nftmaker.py
Python3 script to generate images for NFT projects using wand and ImageMagick

# Dependencies
To use this script, you require the following dependencies:

        - ImageMagick
        - the Wand library for Python (a Python binding for ImageMagick)
        - Python 3.x

# Usage
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
Examples: NFTMaker.py -b base -n 10000

# Author
Vijeet Yarlagadda, vijeetyarla@gmail.com
