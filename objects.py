# Author: Porter Zach
# Python 3.9

import numpy as np

class Object3D:
    def __init__(self):
        pass

    def intersects(self, ray_origin, ray_direction):
        pass

class Sphere(Object3D):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def intersects(self, ray_origin, ray_direction):
        b = 2 * np.dot(ray_direction, ray_origin - self.center)
        c = np.linalg.norm(ray_origin - self.center) ** 2 - self.radius ** 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return None

    def getCenter(self):
        return self.center

    def move(self, x = 0, y = 0, z = 0):
        self.center += np.array([x, y, z])

class Rectangle(Object3D):
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def intersects(self, ray_origin, ray_direction):
        div_inv = []
        # tmin = (self.min[0] - ray_origin[0]) / ray_direction[0] 
        # tmax = (self.max[0] - ray_origin[0]) / ray_direction[0] 
    
        # if tmin > tmax:
        #     tmin, tmax = tmax, tmin
         
        # tymin = (self.min[1] - ray_origin[1]) / ray_direction[1]
        # tymax = (self.max[1] - ray_origin[1]) / ray_direction[1]
    
        # if tymin > tymax:
        #     tymin, tymax = tymax, tymin
    
        # if tmin > tymax or tymin > tmax: 
        #     return None
    
        # if tymin > tmin:
        #     tmin = tymin
    
        # if tymax < tmax:
        #     tmax = tymax
    
        # tzmin = (self.min[2] - ray_origin[2]) / ray_direction[2]
        # tzmax = (self.max[2] - ray_origin[2]) / ray_direction[2]
    
        # if tzmin > tzmax:
        #     tzmin, tzmax = tzmax, tzmin
    
        # if tmin > tzmax or tzmin > tmax:
        #     return None
    
        # if tzmin > tmin:
        #     tmin = tzmin
    
        # if tzmax < tmax:
        #     tmax = tzmax
    
        # return np.linalg.norm(np.array([tmin, tymin, tzmin]))

        # https://tavianator.com/2015/ray_box_nan.html
        t1 = (self.min[0] - ray_origin[0]) / ray_direction[0]
        t2 = (self.max[0] - ray_origin[0]) / ray_direction[0]

        tmin = min(t1, t2)
        tmax = max(t1, t2)

        for i in range(3):
            t1 = (self.min[i] - ray_origin[i]) / ray_direction[i]
            t2 = (self.max[i] - ray_origin[i]) / ray_direction[i]

            tmin = max(tmin, min(t1, t2))
            tmax = min(tmax, max(t1, t2))

        # return tmax > max(tmin, 0.0)
        if not(tmax > max(tmin, 0)):
            return None
        return tmin
    
    def getCenter(self):
        return self.min + ((self.max - self.min) / 2)

    def move(self, x = 0, y = 0, z = 0):
        self.min += np.array([x, y, z])
        self.max += np.array([x, y, z])