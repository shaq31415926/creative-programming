# Reference: https://www.youtube.com/watch?v=eLfRSAgXNZU

import pygame as pg
import cv2

def get_image(path, rgb=True):
    image = cv2.imread(path)
    transposed_image = cv2.transpose(image)
    if rgb == True:
        # get image in rgb format
        image = cv2.cvtColor(transposed_image, cv2.COLOR_RGB2BGR)
    else:
        # otherwise black and white format
        image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)

    return image


def resize_cv2_image(image):
    resized_image = cv2.resize(image, (640, 360), interpolation=cv2.INTER_AREA)
    cv2.imshow("resized cv image", resized_image)


def draw_converted_image(image, ascii_chars, font_size, surface):
    # the image has to be in black and white for this to work
    height = image.shape[1]
    width = image.shape[0]

    ascii_coeff = 255 // (len(ascii_chars) - 1)
    font = pg.font.SysFont("Courier", font_size, bold=True)
    char_step = int(font_size * 0.6)
    rendered_ascii_chars = [font.render(char, False, 'white') for char in ascii_chars]

    char_indices = image // ascii_coeff
    for x in range(0, width, char_step):
        for y in range(0, height, char_step):
            char_index = char_indices[x, y]
            if char_index:
                surface.blit(rendered_ascii_chars[char_index], (x, y))

def save_image(surface, file_path):
    pygame_image = pg.surfarray.array3d(surface)
    cv2_img = cv2.transpose(pygame_image)
    cv2.imwrite(file_path, cv2_img)