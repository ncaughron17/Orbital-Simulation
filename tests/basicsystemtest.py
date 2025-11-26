import sys
import time
import turtle
sys.path.append("./")
from classes.System import system
from classes.Object import object
from classes.Cluster import Cluster


env = system(1000, 800)
#e = object("e", 8, 10e12, (-150,0), (-110,190), env, "red", False)
#f = object("f", 8, 10e12, (-130,0), (-110,190),  env, "red", False)
#a = object("a", 8, 10e12, (-140,10), (-110,190),  env, "red", False)
#b = object("b", 8, 10e12, (-140,20), (-110,190),  env, "red", False)
#c = object("c", 8, 10e12, (-140,-10), (-110,190),  env, "red", False)
#d = object("d", 8, 10e12, (-150,-10), (-110,190),  env, "red", False)
#g = object("g", 8, 10e12, (-150,5), (-110,190), env, "red", False)
#h = object("h", 8, 10e12, (-155,-5), (-110,190), env, "red", False)
#i = object("i", 8, 10e12, (-145,15), (-110,190), env, "red", False)
#j = object("j", 8, 10e12, (-135,-15), (-110,190), env, "red", False)
#k = object("k", 8, 10e12, (-145,12), (-110,190), env, "red", False)
#l = object("l", 8, 10e12, (-135,-5), (-110,190), env, "red", False)

#orbiting_body = Cluster(70, (-190, 0), 20, 5, 10e11, (-50, 180), "red", env) #Interesting config 1
#orbiting_body = Cluster(70, (-290, 0), 20, 5, 10e11, (-50, 180), "red", env) #interesting config 2
orbiting_body = Cluster(70, (-290, 0), 20, 5, 10e11, (-300, 800), "yellow", env) #massive cluster to simulate star orbit, forming accretion disk



#sun = object("sun", 15, 10e14, (0,0), (0,0), env, "yellow", True) #interesting config 1
#sun = object("sun", 15, 20e14, (0,0), (0,0), env, "yellow", True) #interesting config 2
sun = object("sun", 15, 400e14, (0,0), (0,0), env, "grey", True) #extreme gravity, akin to a small black hole

#print(env.objects)

env.runSim()

#turtle.done()