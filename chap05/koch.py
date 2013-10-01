from swampy.TurtleWorld import *

def koch(T, length):
	if length<3:
		fd(T,length)
	else:
		l = length/3
		koch(T,l)
		lt(T,60)
		koch(T,l)
		rt(T,120)
		koch(T,l)
		lt(T,60)
		koch(T,l)

def snowflake(T,length):
	for i in range(0,3):
		koch(T,length)
		rt(T,120)

def cesaro(T,length,angle):
	if length<10:
		fd(T,length)
	else:
		l = length/3
		cesaro(T,l,angle)
		lt(T,angle)
		cesaro(T,l,angle)
		rt(T,angle*2)
		cesaro(T,l,angle)
		lt(T,angle)
		cesaro(T,l,angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = .01

cesaro(bob,500,80)

wait_for_user()

