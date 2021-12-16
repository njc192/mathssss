import math

def distance(x1,y1,x2,y2):
	val = x2-x1
	v2  = y2 - y1
	return math.sqrt(pow(val,2) + pow(v2,2))



def triangle_lengths(x1,y1,x2,y2,x3,y3):
	ab = distance(x1,y1,x2,y2)
	ac = distance(x1,y1,x3,y3)
	bc = distance(x2,y2,x3,y3)

	return ab,ac,bc

def perimeter(arr):
	total = 0
	for val in arr:
		total += val

	return total



def area_circle(rad):
	return 3.14*rad*rad

def circumference(rad):
	return 2*3.14*rad
arr = triangle_lengths(7,-2,-2,7,-6,-6)


def discriminant(a,b,c):
	return pow(b,2)-4*a*c




print(discriminant(3,-7,-4))

