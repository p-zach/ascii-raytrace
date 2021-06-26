# Author: Porter Zach
# Python 3.9

import numpy as np
import render
from objects import Sphere, Rectangle
import time

ramp = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."[::-1] # no space

width = 120
height = 60

max_dist = 15

camera = np.array([0, 0, 1])

# objects = [
#     { 'center': np.array([-0.2, 0, -2]), 'radius': 0.7 },
#     { 'center': np.array([0.2, -0.5, -1]), 'radius': 0.6 },
#     { 'center': np.array([-0.8, 0, 0]), 'radius': 0.2 }
# ]
objs = [
    # Sphere(np.array([-0.2, 0, -2]), 0.7),
    Sphere(np.array([0, .5, -2]), 0.6),
    Rectangle(np.array([-5, -2, -7]), np.array([-4, 5, -3])),
    Rectangle(np.array([4, -2, -7]), np.array([5, 5, -3]))
]
light = { 'position': np.array([2, 4, 4]) }

render.render(width, height, max_dist, camera, light, objs, ramp)

obj = objs[0]

controllable = False

max_right = 3
max_left = -3
speed = .5
dir = 1

while True:
    if controllable:
        inp = input()

        if inp == "a":
            obj.move(x = -1)
        if inp == "d":
            obj.move(x = 1)
        if inp == "q":
            obj.move(y = -1)
        if inp == "e":
            obj.move(y = 1)
        if inp == "s":
            obj.move(z = -1)
        if inp == "w":
            obj.move(z = 1)
    else:
        obj.move(x = speed * dir)
        if not (max_left < obj.getCenter()[0] < max_right):
            dir *= -1

    render.render(width, height, max_dist, camera, light, objs, ramp)