import sys
import time
import turtle
sys.path.append("./")
from classes.System import system
from classes.Object import object


env = system(800, 600)
big = object("big", 20, 10e13, (-100,100), (0,-30), env, "blue", False)
small = object("small", 5, 10e13, (100,0), (0,30),  env, "red", False)

#print(env.objects)

env.runSim()

turtle.done()