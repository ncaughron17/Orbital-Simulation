import turtle

class system:
    def __init__(self, width, height):
        self.system = turtle.Screen()
        self.system.tracer(0)
        self.system.setup(width, height)
        self.system.bgcolor("black")

        self.objects = []

    def addObject(self):
        self.objects.append()#TODO append item of type Object

    def removeObject(self):
        self.objects.remove()#TODO add rmeove item of type Object