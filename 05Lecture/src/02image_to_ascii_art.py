# Reference: https://www.youtube.com/watch?v=eLfRSAgXNZU

import pygame as pg
import cv2
from helpers import get_image, draw_converted_image, save_image

# use cv library to import image, video or even access webcam
# read the image
path = "../image/marguerite-729510_1280.jpeg"
#image = cv2.imread(path)
image = get_image(path, rgb=False)

# resolution of the image
height = image.shape[1]
width = image.shape[0]
res = width, height

# initialise pygame
pg.init()

# set the pygame window name and resolution
surface = pg.display.set_mode(res)
pg.display.set_caption('pygame image')

font_size = 12
ascii_chars = ' .",:;!~+-xmo*#W&8@'

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    # create a black background, white will not work right now
    surface.fill("black")
    draw_converted_image(image, ascii_chars, font_size, surface)
    pg.display.flip()
    # launch the image using cv for comparison
    cv2.imshow("cv image", image)
    # could also resize the image when viewing
    save_image(surface, "image/flower.png")
