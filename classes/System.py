import turtle
import time
import math
import numpy as np

class system:
    def __init__(self, width, height, simTime):
        self.system = turtle.Screen()
        self.system.tracer(0)
        self.system.setup(width, height)
        self.system.bgcolor("black")

        self.statBlock = turtle.Turtle()
        self.statBlock.hideturtle()
        self.statBlock.penup()
        self.statBlock.color("white")
        self.statBlock.goto(-width//2 + 10, height//2 - 30)

        self.lastInterval = 0
        #self.timeInterval = simInterval


        self.objects = []
        self.numObjects = 0
        self.cluster = None
        self.killSim = False
        self.totalFrames = 0 #frames that have accumulated over time
        self.FRAMERATE = 60#frames per second
        self.TOTAL_TIME = simTime#seconds
        self.TOTAL_FRAMES = self.FRAMERATE * self.TOTAL_TIME
        self.timeInterval = 1000 / self.FRAMERATE  # in milliseconds

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
            #obj.drawVelocity()
        self.system.update()

    def calcGrav(self, A: object, B: object, isColliding):
        radiusVec = (B.pos[0] - A.pos[0], B.pos[1] - A.pos[1])
        #print(B.name, B.pos)
        distance = (radiusVec[0]**2 + radiusVec[1]**2)**0.5
        intersectionProportion = 1 - (distance / (A.radius + B.radius))
        forceMag = ((6.67430e-11 * A.mass * B.mass) / (distance**2))
        relVel = np.array((B.vel[0] - A.vel[0], B.vel[1] - A.vel[1]))
        #A.color_ = "yellow"
        #B.color_ = "yellow"
        if isColliding:
            #A.color_ = "red"
            #B.color_ = "red"
            if self.cluster.containsObj(A) is not None and self.cluster.containsObj(B) is not None:
                #forceMag = -( ((6.67430e-11 * A.mass * B.mass) / (intersectionProportion**2)) * 1) - (3000000000* np.sqrt(sum(relVel * relVel))) #(A.radius + B.radius - distance) * 48e10 # simple collision response
                
                forceMag = -(intersectionProportion * 50000000.0) - (400.0* np.sqrt(sum(relVel * relVel)))#alternate dampening, independent of particle mass, not related to gravity
                
                
            else:#destroy smaller object if not in same cluster
                if A.radius < B.radius:
                    A.clear()
                    self.removeObject(A)
                elif B.radius < A.radius:
                    B.clear()
                    self.removeObject(B)
            
        # if (distance < 2):
        #     forceMag = 0
        forceVec = (forceMag * radiusVec[0]/distance, forceMag * radiusVec[1]/distance)

        dt = self.timeInterval / 1000.0
        A.updateVel((forceVec[0]/A.mass * dt, forceVec[1]/A.mass * dt))
        #A.updateAcc(self.lastInterval)
        B.updateVel((-forceVec[0]/B.mass * dt, -forceVec[1]/B.mass * dt))
        #B.updateAcc(self.lastInterval)

        

        #if self.cluster is not None: #UNCOMMENT IF YOU WANT CLUSTER VELOCITY VECTOR
             #self.cluster.updateClusterPos()
             #self.cluster.updateClusterVel()
             #self.cluster.drawClusterVector()
             

    def checkCollision(self, A: object, B: object):
        radiusVec = (B.pos[0] - A.pos[0], B.pos[1] - A.pos[1])
        distance = (radiusVec[0]**2 + radiusVec[1]**2)**0.5
        if distance <= A.radius + B.radius:
            return True
        return False

    def calcAllGravAndColl(self):
        n = len(self.objects)
        for i in range(n):
            for j in range(i + 1, n):
                A = self.objects[i]
                B = self.objects[j]
                self.calcGrav(A, B, self.checkCollision(A, B))

    def updateAll(self, timeInterval):
        self.calcAllGravAndColl()
        for obj in self.objects:
            obj.updatePos(timeInterval)
            
    def saveAndCheckFrame(self, frameNum):
        #print(self.totalFrames)
        #print(frameNum)
        if frameNum > self.totalFrames:
            self.system.getcanvas().postscript(file=f"frames_ps/frame_{self.totalFrames:05d}.ps", colormode='color',width=2560, height=1440)
            self.totalFrames += 1
            #print("in the if")
        elif frameNum == self.totalFrames:
            #print("in the else")
            self.stopSim()

    def runSim(self):
        self.killSim = False
        #lastTime = time.time()
        while not self.killSim:
            currentTime = time.time()
            #timeInterval = (currentTime - lastTime) * 1000  # in milliseconds
            #self.lastInterval = self.timeInterval
            self.updateAll(self.timeInterval)
            self.drawAll()
            self.saveAndCheckFrame(self.TOTAL_FRAMES)

           #lastTime = currentTime
            #print(self.objects[0].vel)
            # while (time.time() - currentTime) * 1000 < 16:
            #     pass  # busy-wait to maintain ~60 FPS

    def stopSim(self):  
        self.killSim = True

    