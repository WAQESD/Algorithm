from sys import stdin
n = int(stdin.readline())
stones = list(map(int, stdin.readline().split()))
m = 3 * (10 ** 6)
m2 = 34
dp = [0] * (m+1)
fibo = [0] * m2
fibo[0] = 1
fibo[1] = 2
for i in range(2, m2): fibo[i] = fibo[i-1] + fibo[i-2]
for i in range(1, m+1):
	visited = [False] * m2
	for j in range(m2):
		if(i-fibo[j] < 0): break
		visited[dp[i - fibo[j]]] = True
	for j in range(m2):
		if(not visited[j]):
			dp[i] = j
			break

result = bool(0)
for stone in stones: result ^= bool(dp[stone])
print(result)
print('koosaga' if result else 'cublover')