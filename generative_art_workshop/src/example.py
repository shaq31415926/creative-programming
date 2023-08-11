#!/usr/bin/env python
import os
import sys

from PIL import Image
import neuralart

# if a directory is not specified, use a directory called images
if len(sys.argv) != 2:
    directory = "images"
else:
    directory = sys.argv[1]

# create the directory if the directory does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# specify some initial parameters
RENDER_SEED = 4
ITERATIONS = 150
RESOLUTION = 1024
Z_DIMS = 6
step_size = 2.0 / ITERATIONS

# each iteration we will adjust the z value
# which I am assuming represents the values from the neurons of the output layer.
z = [-1.0] * Z_DIMS

for x in range(ITERATIONS):
    # this uses the neural art render function which can be found here:
    # https://github.com/dstein64/neuralart/blob/master/neuralart/neuralart.py

    result = neuralart.render(
        xres=RESOLUTION,
        seed=RENDER_SEED,
        channels=3,
        z=z
    )

    # writes each file to the folder
    file = os.path.join(directory, f"{x}.png")
    im = Image.fromarray(result.squeeze())
    im.save(file, 'png')
    z = [_z + step_size for _z in z]
    print(z)
