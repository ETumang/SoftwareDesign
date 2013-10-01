"""Finds if a is a power of b. 

a:positive integer

b:positive integer

returns:boolean
"""
def power(a,b):
	if a == b:
		return True
	elif not a%b ==0:
		print a%b
		return False
	else:
		print a//b
		return power(a//b,b)

"""Finds the greatest common divisor of numbers a and b.

a: positive integer

b: positive integer

returns:integer
"""
def gcd(a,b):
	if b == 0:
		return a;
	else:
		return gcd(b, a%b)






