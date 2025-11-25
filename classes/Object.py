import turtle
from classes.System import system

class object(turtle.Turtle):

    def __init__(self, name, radius, mass, pos: tuple, vel: tuple, _System: system, color, isStatic):
        super().__init__(shape="circle")
        self.radius = radius
        self.isStatic = isStatic
        self.color_ = color
        self.name = name
        self.vel = vel
        self.pos = pos
        self.mass = mass

        self.penup()
        self.hideturtle()
        _System.addObject(self)


    def updateVel(self, vel):
        if(not self.isStatic):
            self.vel = (self.vel[0] + vel[0], self.vel[1] + vel[1])
        

    def updatePos(self, timeInterval):
        self.pos = [self.pos[0] + self.vel[0] * timeInterval/1000, self.pos[1] + self.vel[1] * timeInterval/1000]

    def draw(self):
        self.clear()
        self.goto(self.pos[0], self.pos[1])
        self.dot(self.radius*2, self.color_)
        self.penup()
        self.drawVelocity()

    def drawVelocity(self):
        self.width(3)
        self.color("white")
        self.pendown()
        self.goto(self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        self.penup()