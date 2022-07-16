from sys import stdin
import math
INF = 10**9
def ccw(a, b, c):
	return (b[0] - a[0])*(c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def dist(a, b, c):
	v1 = [a[0] - b[0], a[1] - b[1]]
	nv1 = math.sqrt(v1[0]**2 + v1[1]**2)
	v2 = [a[0] - c[0], a[1] - c[1]]
	nv2 = math.sqrt(v2[0]**2 + v2[1]**2)
	cos = (v1[0]*v2[0] + v1[1]*v2[1]) / (nv1 * nv2)
	return nv2 * math.sqrt(1 - cos**2)

while(True):
	n = int(stdin.readline())
	if(n==0): break
	points = []
	result = INF
	for i in range(n): points.append(list(map(int, stdin.readline().split())))
	for i in range(n-1):
		for j in range(i+1, n):
			prev = 0
			check = True
			tmp = 0
			for k in range(n):
				if(k==i or k==j): continue
				now = ccw(points[i], points[j], points[k])
				if(prev * now < 0): 
					check = False
					break
				if(now != 0): prev = now
			if(check):
				for k in range(n):
					if(k==i or k==j): continue
					tmp = max(tmp, dist(points[i], points[j], points[k]))
				result = min(result, tmp)
	dec = result - math.trunc(result)
	dec *= 1000
	dec = math.trunc(dec)
	if(dec % 10): dec += 10
	dec = dec // 10
	dec = dec / 100
	print("{:.2f}".format(math.trunc(result)+dec))