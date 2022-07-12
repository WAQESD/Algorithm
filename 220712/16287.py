from sys import stdin
import sys
w, n = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
case = [0] * w
for i in range(n-1):
	for j in range(i+1, n):
		now = arr[i] + arr[j]
		if(now < w and case[w - now]):
			print("YES")
			sys.exit(0)

	for j in range(i):
		now = arr[i] + arr[j]
		if now < w: case[now] = 1

print("NO")
