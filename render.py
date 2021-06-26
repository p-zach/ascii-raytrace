# Functions normalize, sphere_intersect, nearest_intersected_object, and render are
# provided by Omar Aflak's "Ray Tracing From Scratch in Python" Medium tutorial.
# https://medium.com/swlh/ray-tracing-from-scratch-in-python-41670e6a96f9

import numpy as np
import sys

def normalize(vector):
    return vector / np.linalg.norm(vector)

def nearest_intersected_object(objects, ray_origin, ray_direction):
    distances = [obj.intersects(ray_origin, ray_direction) for obj in objects]
    nearest = None
    min_dist = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_dist:
            min_dist = distance
            nearest = objects[index]
    return nearest, min_dist

def render(width, height, max_dist, camera, light, objects, ramp):
    ratio = float(width) / height
    screen = (-1, 1 / ratio, 1, -1 / ratio) # left top right bottom

    s = ''
    for i, y in enumerate(np.linspace(screen[1], screen[3], height // 2)):
        s = ''
        for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
            pixel = np.array([x, y, 0])
            origin = camera
            direction = normalize(pixel - origin)

            # check intersections
            nearest_object, distance = nearest_intersected_object(objects, origin, direction)
            if nearest_object is None:
                s += ' '
                continue
            
            # char = ramp[int(min(distance / max_dist, 1) * len(ramp)) - 1]
            # s += char
            # continue

            # compute intersection point between ray and nearest objects
            intersection = origin + distance * direction

            # shifts intersection point away from edge to avoid near-boundary errors
            normal = normalize(intersection - nearest_object.getCenter())
            shifted = intersection + 1e-5 * normal
            intersection_to_light = normalize(light['position'] - shifted)

            _, distance = nearest_intersected_object(objects, shifted, intersection_to_light)
            intersection_to_light_distance = np.linalg.norm(light['position'] - intersection)
            is_shadowed = distance < intersection_to_light_distance

            char = ramp[0]

            if not is_shadowed:
                char = ramp[int(min(intersection_to_light_distance / max_dist, 1) * len(ramp)) - 1]

            s += char
        sys.stdout.write(s)
    sys.stdout.flush()