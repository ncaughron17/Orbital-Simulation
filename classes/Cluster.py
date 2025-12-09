import math
import numpy as np
from classes.Object import object
from classes.System import system
import turtle

class Cluster:
    def __init__(self, num, center, clusterRadius_, objectRadius_, objectMass_, initVel_, color_, system_: system):
        self.objects = self.generateCluster(num, center, clusterRadius_, objectRadius_, objectMass_, initVel_, color_, system_)
        self.avg_velocity = ()
        self.center_of_mass = ()
        system_.addCluster(self)
        self.vectorPen = turtle.Turtle()
        self.vectorPen.penup()
        self.vectorPen.hideturtle()


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
    
    def drawClusterVector(self):
        scale = 0.1#scaling for arrow length, for visibility
        self.vectorPen.clear()
        self.vectorPen.width(3)
        self.vectorPen.color("white")
        self.vectorPen.goto(self.center_of_mass[0], self.center_of_mass[1])
        self.vectorPen.pendown()
        self.vectorPen.goto((self.center_of_mass[0] + scale * self.avg_velocity[0]), (self.center_of_mass[1] + scale * self.avg_velocity[1]))
        self.vectorPen.penup()

    def updateClusterVel(self):
        xAvg  = 0
        yAvg = 0
        for obj in self.objects:
            xAvg = xAvg + (obj.vel[0])
            yAvg = yAvg + (obj.vel[1])
        self.avg_velocity = np.asarray((xAvg/len(self.objects), yAvg/len(self.objects)))
        
    def updateClusterPos(self):
        xAvg  = 0
        yAvg = 0
        for obj in self.objects:
            xAvg = xAvg + (obj.pos[0])
            yAvg = yAvg + (obj.pos[1])
        self.center_of_mass = np.asarray((xAvg/len(self.objects), yAvg/len(self.objects)))
        
            

    
