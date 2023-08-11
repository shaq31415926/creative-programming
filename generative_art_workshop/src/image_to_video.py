import sys
import cv2

import os
import glob

# reference: https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/

img_array = []

if len(sys.argv) != 2:
    directory = "images"
else:
    directory = sys.argv[1]


def get_key(fp):
    """This function will order the key by numerical order"""
    filename = os.path.splitext(os.path.basename(fp))[0]
    int_part = filename.split()[0]
    return int(int_part)


for filename in sorted(glob.glob(f'{directory}/*.png'), key=get_key):
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

# create the video directory if the directory does not exist
if not os.path.exists("video"):
    os.makedirs("video")

out = cv2.VideoWriter('video/example.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
