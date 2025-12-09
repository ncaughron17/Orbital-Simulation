import turtle
from classes.System import system
import numpy as np

class object(turtle.Turtle):

    def __init__(self, name, radius, mass, pos: tuple, vel: tuple, _System: system, color, isStatic):
        super().__init__(shape="circle")
        self.radius = radius
        self.isStatic = isStatic
        self.color_ = color
        self.name = name
        self.vel = np.asarray(vel)
        self.pos = np.asarray(pos)
        self.mass = mass
        self.acc = np.asarray((0,0))
        self.lastVel = (0,0)
        #self.prev

        self.penup()
        self.hideturtle()
        _System.addObject(self)


    def updateVel(self, vel):
        if(not self.isStatic):
            self.lastVel = self.vel
            self.vel = (self.vel[0] + vel[0], self.vel[1] + vel[1])

        
    def updatePos(self, timeInterval):
        self.pos = [self.pos[0] + self.vel[0] * timeInterval/1000, self.pos[1] + self.vel[1] * timeInterval/1000]

    def updateAcc(self, interval):
        self.acc = np.asarray((self.vel[0] - self.lastVel[0]) / interval,(self.vel[0] - self.lastVel[0]) / interval)

    def draw(self):
        self.clear()
        self.goto(self.pos[0], self.pos[1])
        self.dot(self.radius*2, self.color_)
        self.penup()
        #self.drawVelocity()

    def drawVelocity(self):
        self.width(3)
        self.color("white")
        self.pendown()
        self.goto(self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        self.penup()