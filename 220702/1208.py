from sys import stdin
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
result = 0
for i in range(n):
	for j in range(i, n):
		if(s == sum(arr[i:j+1])): result += 1

print(result)


"""
6 0
-7 -3 -2 0 5 7

from sys import stdin
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
cache = [[0] * n for _ in range(n)]
result = 0
for i in range(n): 
	cache[i][i] = arr[i] 
	if(arr[i] == s): result += 1 
for i in range(1, n+1):
	for left in range(n-i):
		cache[left][left+i] = arr[left] + cache[left+1][left+i]
		if(cache[left][left+i] == s): result +=1

print(result)

"""