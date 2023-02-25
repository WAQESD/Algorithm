from sys import stdin

n, k, d = map(int, stdin.readline().split())
students = []
alg = [0] * (k+1)

for i in range(n):
	num, skill = map(int, stdin.readline().split())
	algorithms = set(map(int, stdin.readline().split()))
	students.append([skill, algorithms])

students.sort()

l = 0
r = 0
E = 0

while(l < n):
	while(r < n and students[r][0] - students[l][0] <= d):
		for algorithm in students[r][1]:
			alg[algorithm] += 1
		r += 1
	e = 0
	for i in range(k+1):
		if(0 < alg[i] < (r-l)): e += 1
		
	E = max(E, e * (r-l))
	
	for algorithm in students[l][1]:
		alg[algorithm] -= 1

	l += 1

print(E)