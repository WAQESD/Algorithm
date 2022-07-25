from sys import stdin

N, K = map(int, stdin.readline().split())
mod = 1000000007

def factorial(n):
	result = 1
	for i in range(2, n+1):
		result = (result * i) % mod
	return result

def exp(n, k):
	if(k == 0): return 1
	if(k == 1): return n
	tmp = exp(n, k//2)
	if(k % 2): return tmp * tmp * n % mod
	else: return tmp * tmp % mod

numerator = factorial(N)
denominator = factorial(N-K) * factorial(K) % mod
print(numerator * exp(denominator, mod-2) % mod)