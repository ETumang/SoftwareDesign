from swampy.TurtleWorld import *

"""Draws a dragon curve.  Must be used with drawFig.

T: Turtle

Length: positive numeric

Depth: positive integer

Return: none
"""
def turnright(T,length,depth):
        if depth==0:
            fd(T,length)
        else:
            turnright(T,length,depth-1)
            rt(T)
            drawFig(T,length,depth-1)

"""Draws a dragon curve. Must be used with turnright.

T: turtle

Length: positive numeric

Depth: positive integer

Return: none
"""
def drawFig(T,length,depth):
    if depth==0:
        fd(T,length)
    else:
        turnright(T,length,depth-1)
        lt(T)
        drawFig(T,length,depth-1)

"""Draws a dragon curve using turnright and drawfig.

T: turtle

Depth: positive integer

Return: none
"""

def dragon(T,depth)
world = TurtleWorld()
bob = Turtle()
bob.delay = .01

wait_for_user()