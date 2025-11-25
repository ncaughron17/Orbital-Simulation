import sys
import time
import turtle
sys.path.append("./")
from classes.System import system
from classes.Object import object


env = system(1000, 800)
e = object("e", 8, 10e12, (-150,0), (-100,170), env, "blue", False)
f = object("f", 8, 10e12, (-130,0), (-100,170),  env, "red", False)
a = object("a", 8, 10e12, (-140,10), (-100,170),  env, "red", False)
b = object("b", 8, 10e12, (-140,20), (-100,170),  env, "red", False)
c = object("c", 8, 10e12, (-140,-10), (-100,170),  env, "red", False)
d = object("d", 8, 10e12, (-150,-10), (-100,170),  env, "red", False)
g = object("g", 8, 10e12, (-150,5), (-100,170), env, "red", False)
h = object("h", 8, 10e12, (-155,-5), (-100,170), env, "red", False)
i = object("i", 8, 10e12, (-145,15), (-100,170), env, "red", False)
j = object("j", 8, 10e12, (-135,-15), (-100,170), env, "red", False)
k = object("k", 8, 10e12, (-145,12), (-100,170), env, "red", False)
l = object("l", 8, 10e12, (-135,-5), (-100,170), env, "red", False)



smthElse = object("smthElse", 15, 5e14, (0,0), (0,0), env, "green", True)

#print(env.objects)

env.runSim()

turtle.done()