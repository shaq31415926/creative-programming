# Reference: https://www.youtube.com/watch?v=eLfRSAgXNZU

import pygame as pg
import cv2
from helpers import get_image, draw_converted_image

# use cv library to import image, video or even access webcam
# read the image
path = "../image/marguerite-729510_1280.jpeg"
image = cv2.imread(path)
# image = get_image(path, rgb=False)

# resolution of the image
height = image.shape[1]
width = image.shape[0]
res = width, height

# initialise pygame
pg.init()

# set the pygame window name and resolution
surface = pg.display.set_mode(res)
pg.display.set_caption('pygame image')

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    # launch the image using pygame
    pg.surfarray.blit_array(surface, image)
    pg.display.flip()
    # launch the image using cv
    cv2.imshow("cv image", image)
