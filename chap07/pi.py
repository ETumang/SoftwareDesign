import math
from math import factorial


def estimate_pi():
"""Uses an infinite series to estimate pi.

Return: float
"""

    k = 0
    t = (factorial(4*k)*(1103+26390*k))/(factorial(k)**4*396**(4*k))
    estimate = t

    while t>1e-15:
        k = k+1
        t = (factorial(4*k)*(1103+26390*k))/(factorial(k)**4*396**(4*k))
        estimate = estimate+t


    inverse = estimate*((2.0*math.sqrt(2))/9801)

    return (1/inverse)

p = estimate_pi()
print p
print math.pi-p