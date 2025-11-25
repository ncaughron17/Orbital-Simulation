import turtle
import time

class system:
    def __init__(self, width, height):
        self.system = turtle.Screen()
        self.system.tracer(0)
        self.system.setup(width, height)
        self.system.bgcolor("black")

        self.objects = []

    def addObject(self, obj):
        self.objects.append(obj)#TODO append item of type Object

    def removeObject(self, obj):
        self.objects.remove(obj)#TODO add rmeove item of type Object

    def drawAll(self):
        for obj in self.objects:
            obj.draw()
        self.system.update()

    def calcGrav(self, A: object, B: object):
        radiusVec = (B.pos[0] - A.pos[0], B.pos[1] - A.pos[1])
        #print(B.name, B.pos)
        distance = (radiusVec[0]**2 + radiusVec[1]**2)**0.5
        forceMag = (6.67430e-11 * A.mass * B.mass) / (distance**2)
        forceVec = (forceMag * radiusVec[0]/distance, forceMag * radiusVec[1]/distance)
        A.updateVel((forceVec[0]/A.mass, forceVec[1]/A.mass))
        B.updateVel((-forceVec[0]/B.mass, -forceVec[1]/B.mass))

    def calcAllGrav(self):
        for A in self.objects:
            checkList = self.objects.copy()
            checkList.remove(A)
            for B in checkList:
                self.calcGrav(A, B)

    def updateAll(self, timeInterval):
        self.calcAllGrav()
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
            print(self.objects[0].vel)
            while (time.time() - currentTime) * 1000 < 16:
                pass  # busy-wait to maintain ~60 FPS