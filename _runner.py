#!/usr/bin/python3

from deoldify import device
from deoldify.device_id import DeviceId

#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

from deoldify.visualize import *
import warnings

import sys
import os

warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

render_factor = 35

input_dir = sys.argv[1]
output_dir = sys.argv[2]

if not os.path.isdir(input_dir):
    print("input directory is not a directory or not exist")
    sys.exit(1)

if os.path.exists(output_dir):
    print("out directory is already exist")
    sys.exit(1)

os.makedirs(output_dir)

colorizer = get_image_colorizer(artistic=True)
for filename in os.listdir(input_dir):
    f = os.path.join(input_dir, filename)
    if os.path.isfile(f) and (f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg")):
        image_path = colorizer.plot_transformed_image(path=f,
                                                      results_dir=Path(output_dir),
                                                      render_factor=render_factor,
                                                      compare=True,
                                                      watermarked=False)
        print("{} ready".format(image_path))

