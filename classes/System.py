import turtle
import time
import math
import numpy as np

class system:
    def __init__(self, width, height):
        self.system = turtle.Screen()
        self.system.tracer(0)
        self.system.setup(width, height)
        self.system.bgcolor("black")

        self.statBlock = turtle.Turtle()
        self.statBlock.hideturtle()
        self.statBlock.penup()
        self.statBlock.color("white")
        self.statBlock.goto(-width//2 + 10, height//2 - 30)

        self.objects = []
        self.numObjects = 0
        self.cluster = None

    def addCluster(self, cluster):
        #self.clusters.append(cluster)
        self.cluster = cluster

    def addObject(self, obj):
        self.objects.append(obj)#TODO append item of type Object
        self.updateObjCount(self.numObjects + 1)

    def updateObjCount(self, count):
        self.numObjects = count
        self.statBlock.clear()
        self.statBlock.pendown()
        self.statBlock.write(f"Objects: {self.numObjects}", align="left", font=("Arial", 16, "normal"))
        self.statBlock.penup()

    def removeObject(self, obj):
        self.objects.remove(obj)#TODO add rmeove item of type Object
        self.updateObjCount(self.numObjects - 1)
        if self.cluster is not None:
            if obj in self.cluster.objects:
                self.cluster.objects.remove(obj)

    def drawAll(self):
        for obj in self.objects:
            obj.draw()
        self.system.update()

    def calcGrav(self, A: object, B: object, isColliding):
        radiusVec = (B.pos[0] - A.pos[0], B.pos[1] - A.pos[1])
        #print(B.name, B.pos)
        distance = (radiusVec[0]**2 + radiusVec[1]**2)**0.5
        forceMag = ((6.67430e-11 * A.mass * B.mass) / (distance**2))
        if isColliding:
            if self.cluster.containsObj(A) is not None and self.cluster.containsObj(B) is not None:
                #print(forceMag)
                forceMag = -(forceMag * 1) - (A.radius + B.radius - distance) * 45e10 # simple collision response
                
            else:
                if A.radius < B.radius:
                    A.clear()
                    self.removeObject(A)
                elif B.radius < A.radius:
                    B.clear()
                    self.removeObject(B)
            
        if (distance < 2):
            forceMag = 0
        forceVec = (forceMag * radiusVec[0]/distance, forceMag * radiusVec[1]/distance)
        
        A.updateVel((forceVec[0]/A.mass, forceVec[1]/A.mass))
        B.updateVel((-forceVec[0]/B.mass, -forceVec[1]/B.mass))

    def checkCollision(self, A: object, B: object):
        radiusVec = (B.pos[0] - A.pos[0], B.pos[1] - A.pos[1])
        distance = (radiusVec[0]**2 + radiusVec[1]**2)**0.5
        if distance <= A.radius + B.radius:
            return True
        return False

    def calcAllGravAndColl(self):
        for A in self.objects:
            checkList = self.objects.copy()
            checkList.remove(A)
            for B in checkList:
                self.calcGrav(A, B, self.checkCollision(A, B))

    def updateAll(self, timeInterval):
        self.calcAllGravAndColl()
        for obj in self.objects:
            obj.updatePos(timeInterval)
            
    

    def runSim(self):
        
        lastTime = time.time()
        while True:
            currentTime = time.time()
            timeInterval = (currentTime - lastTime) * 1000  # in milliseconds
            self.updateAll(timeInterval)
            self.drawAll()
            lastTime = currentTime
            #print(self.objects[0].vel)
            while (time.time() - currentTime) * 1000 < 16:
                pass  # busy-wait to maintain ~60 FPS