#A solution to Exercise 3.5 in Think Python.  Creates a grid of size mxn.
#Emily Tumang 9/22/13

def grid(numRows, numCols):
    for i in range (0,numRows):
        println(numCols)
        printrow(4,numCols)
    println(numCols) 

def printchar(a,num):
   for i in range (0,num):
       print a,

def println(cols):
    for i in range (0,cols):
        print '+',
        printchar('-',4)
    print '+'

def printrow(height, ncols):
    for i in range (0,height):
        for i in range(0,ncols+1):
            printchar('|',1)
            printchar(' ',4)
        print
    
grid(4,4)      




