from sys import stdin
from math import sqrt
n = int(stdin.readline())
points = [[]] * n
for i in range(n): points[i] = list(map(int, stdin.readline().split()))

def CCW(a, b, c):
	return (b[0] - a[0]) * (c[1]-a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def isInTriangle(v2, v3, v1, point):
	d1 = [v2[0] - v1[0], v2[1] - v1[1]]
	d2 = [v3[0] - v1[0], v3[1] - v1[1]]
	k = [point[0] - v1[0], point[1] - v1[1]]

	alpha = (d2[0] * k[1] - d2[1] * k[0]) / (d2[0] * d1[1] - d2[1] * d1[0])
	beta = (d1[0] * k[1] - d1[1] * k[0]) / (d1[0] * d2[1] - d2[0] * d1[1])

	if(0 <= alpha and alpha <= 1 and 0 <= beta and beta <= 1 and alpha + beta <= 1): return True
	else: return False

def getDistance(p, q, r):
	a = p[1] - q[1]
	b = q[0] - p[0]
	c = p[0] * (q[1] - p[1]) - p[1] * (q[0] - p[0])
	return abs(a*r[0] + b*r[1] + c) / sqrt(a**2 + b**2)

def QuickHull(points):
	points.sort()
	a = points[0]
	b = points[-1]
	points = points[1:-1]
	S1 = []
	S2 = []
	for point in points:
		ccw = CCW(a, b, point)
		if(ccw > 0.00): S2.append(point)
		elif(ccw < 0.00): S1.append(point)
	result = 2
	result += FindHull(S1, a, b)
	result += FindHull(S2, b, a)
	return result

def FindHull(S, a, b):
	if(len(S) == 0): return 0
	if(len(S) == 1): return 1
	dist = 0
	C = [0,0]
	for point in S:
		d = getDistance(a, b, point)
		if(d > dist):
			dist = d
			C = point
	result = 1
	S1 = []
	S2 = []

	for point in S:
		if(point[0] == C[0] and point[1] == C[1]): continue
		if(isInTriangle(C, a, b, point)): continue
		ccw = CCW(a, C, point)
		if(ccw < 0.00): S1.append(point)
		elif(ccw > 0.00): S2.append(point)
	
	result += FindHull(S1, a, C)
	result += FindHull(S2, C, b)
		
	return result

if(n == 3): print(3)
else: print(QuickHull(points))