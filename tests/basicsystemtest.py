import sys
import time
import turtle
sys.path.append("./")
from classes.System import system
from classes.Object import object
from classes.Cluster import Cluster


env = system(2560, 1440, 10)

#orbiting_body = Cluster(70, (-190, 0), 20, 5, 10e11, (-50, 180), "red", env) #Interesting config 1
#orbiting_body = Cluster(70, (-290, 0), 20, 5, 10e11, (-50, 180), "red", env) #interesting config 2
#orbiting_body = Cluster(40, (-390, 0), 20, 5, 15e11, (-200,700), "yellow", env) #massive cluster to simulate star consumption, forming accretion disk

#sun = object("sun", 15, 10e14, (0,0), (0,0), env, "yellow", True) #interesting config 1
#sun = object("sun", 15, 20e14, (0,0), (0,0), env, "yellow", True) #interesting config 2
#sun = object("sun", 15, 400e14, (0,0), (0,0), env, "grey", True) #extreme gravity, akin to a small black hole

#Orbiting_body = Cluster(30, (-300, 0), 20, 5, 10e11, (0, 180), "red", env)
#sun = object("sun", 15, 10e14, (0,0), (0,0), env, "yellow", True) #interesting config 1

#sun = object("sun", 15, 200e14, (0,0), (0,0), env, "grey", True) #extreme gravity, akin to a small black hole
#orbiting_body = Cluster(200, (-400, 0), 20, 5, 20e11, (0,310), "yellow", env)

body_one = object("body_one", 30, 10e18, (-400,0), (0,-500), env, "red", False)
body_two = object("body_two", 30, 10e18, (400,0), (0,500), env, "blue", False)

#orbiting_body = Cluster(200, (0, 0), 20, 5, 20e11, (0,0), "yellow", env)


#print(env.objects)

env.runSim()

#turtle.done()