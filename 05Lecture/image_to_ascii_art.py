# Reference: https://www.youtube.com/watch?v=eLfRSAgXNZU
import cv2
import pygame as pg
from helpers import get_image, resize_cv2_image, draw_converted_image, save_image

# use cv library to import image, video or even access webcam
# read the image
path = "image/marguerite-729510_1280.jpeg"
# image = cv2.imread(path)
image = get_image(path, rgb=False)

# image parameters
height = image.shape[1]
width = image.shape[0]
res = width, height

# initialise the pygame library
pg.init()
surface = pg.display.set_mode(res)
pg.display.set_caption("pygame image")

ascii_chars = ' .",~+-x:;!mo*#W&8@'
#ascii_chars = " %&//#"
font_style = "Courier"
font_size = 2
background_colour = "black"

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    # launch the image using pygame
    # pg.surfarray.blit_array(surface, image)
    surface.fill(background_colour)
    draw_converted_image(image, ascii_chars, font_style, font_size, surface)
    pg.display.flip()
    # launch our original image
    # cv2.imshow("original image", image)
    resize_cv2_image(image)
    save_image(surface, "image/flowers_ascii_2.png")

