import turtle

class object(turtle.Turtle):

    def __init__(self, name, radius, pos: tuple, color, isStatic):
        self.radius = radius
        self.isStatic = isStatic
        self.color = color
        self.name = name
        self.vel = [0,0]
        self.pos = pos

    def updateVel(self, vel):
        self.vel = vel

    def updatePos(self, timeInterval):
        self.pos = [self.vel[0] * timeInterval/1000, self.vel[1] * timeInterval]