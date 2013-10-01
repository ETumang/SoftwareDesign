from swampy.TurtleWorld import *

"""Draws a Koch curve of length length.  

T: turtle 

length: positive numeric

returns: none
""" 
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

"""Draws a Koch snowflake with sides of length length. 

T: turtle

length: positive numeric

returns: none
"""
def snowflake(T,length):
	for i in range(0,3):
		koch(T,length)
		rt(T,120)

"""Draws a Cesaro curve with length length and internal angles
angle. 

T: turtle

Length: Positive numeric

Angle: Positive numeric

returns: none
"""
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

