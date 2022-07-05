from sys import stdin
n = int(stdin.readline())
x = []
y = []
for i in range(n): 
	nx, ny = map(int, stdin.readline().split())
	x.append(nx)
	y.append(ny)
x = x + [x[0]]
y = y + [y[0]]
answer = 0
for i in range(n):
	answer += x[i] * y[i+1] - x[i+1] * y[i]

print(round(abs(answer) / 2, 1))
