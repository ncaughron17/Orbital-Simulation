import math
import numpy as np
from classes.Object import object
from classes.System import system

class Cluster:
    def __init__(self, num, center, clusterRadius_, objectRadius_, objectMass_, initVel_, color_, system_: system):
        self.objects = self.generateCluster(num, center, clusterRadius_, objectRadius_, objectMass_, initVel_, color_, system_)
        self.avg_velocity = ()
        self.center_of_mass = ()
        system_.addCluster(self)

    def generatePoints(self, clusterRadius, objNum):
        points = []
        phi = (1 + 5**0.5) / 2
        for i in range(objNum):
            theta = 2 * math.pi * i / phi
            r = clusterRadius * (i / objNum)**0.5
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            points.append((x, y))
        return points
    
    def generateCluster(self, objNum, centerPos, clusterRadius, objectRadius, objectMass, initVel, color, system: system):
        points = self.generatePoints(clusterRadius, objNum)
        objects = []
        for obj in range(objNum):
            pos = (centerPos[0] + points[obj][0], centerPos[1] + points[obj][1])
            new_object = object(f"cluster_obj_{obj}", objectRadius, objectMass, pos, initVel, system, color, False)
            objects.append(new_object)
        return objects
    
    def containsObj(self, obj: object):
        if obj in self.objects:
            return obj in self.objects

    
