from sys import stdin
n = int(stdin.readline())
v = []
l = []
for i in range(n):
	v.append(int(stdin.readline()))
	l.append(len(str(v[-1])))
k = int(stdin.readline())
v = [i % k for i in v]
dp = [[-1] * (1<<n) for _ in range(k)]
ten = [1]
for i in range(50): ten.append((ten[-1] * 10) % k)

def dfs(mod, bit):
	if(bit == (1 << n) - 1): return 1 if mod == 0 else 0
	if(dp[mod][bit] > -1): return dp[mod][bit]
	result = 0
	for i in range(n):
		cur = 1 << i
		if(bit & cur): continue
		nxt = ((mod * ten[l[i]]) % k + v[i]) % k
		result += dfs(nxt, bit+cur)
	dp[mod][bit] = result
	return result

def gcd(a, b):
	if(b == 0): return a
	return gcd(b, a % b)

numerator = dfs(0, 0)
denominator = 1
for i in range(1, n+1): denominator *= i
GCD = gcd(denominator, numerator)
print(numerator // GCD, end='')
print('/', end='')
print(denominator // GCD)