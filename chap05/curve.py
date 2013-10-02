from swampy.TurtleWorld import *

def turnright(T,length,depth):
        if depth==0:
            fd(T,length)
        else:
            turnright(T,length,depth-1)
            rt(T)
            drawFig(T,length,depth-1)

def drawFig(T,length,depth):
    if depth==0:
        fd(T,length)
    else:
        turnright(T,length,depth-1)
        lt(T)
        drawFig(T,length,depth-1)

def dragon(T,depth):
    turnright(T,5,depth)


world = TurtleWorld()
bob = Turtle()
bob.delay = .01

dragon (bob, 5)
wait_for_user()