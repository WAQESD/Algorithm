from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
e = [0] * (n+1)
arr.sort()
def exp(x):
	if(x == 0): return 1
	if(x == 1): return 2
	if(e[x] > 0): return e[x]
	half = exp(x//2)
	e[x] = half * half % 1000000007 if x % 2 == 0 else half * half * 2 % 1000000007
	return e[x]

answer = 0
for i in range(n):
	answer += arr[i] * (exp(i) - exp(n-i-1)) 
answer %= 1000000007

print(answer)