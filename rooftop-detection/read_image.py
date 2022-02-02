#!/usr/bin/env python3

from PIL import Image

img = Image.open('data/custom/Medellin_40cm.tif')

print(img.size)
