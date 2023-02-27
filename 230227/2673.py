from sys import stdin

n = int(stdin.readline())
lines = [[0] * 101 for _ in range(101)]
dp = [[0] * 101 for _ in range(101)]

for i in range(n):
    line = list(map(int, stdin.readline().split()))
    lines[line[0]][line[1]] = 1
    lines[line[1]][line[0]] = 1

for i in range(1, 101):
    for j in range(i, 0, -1):
        for k in range(j, i):
            dp[j][i] = max(dp[j][i], dp[j][k] + dp[k][i] + lines[j][i])


print(dp[1][100])