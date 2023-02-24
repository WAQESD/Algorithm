from sys import stdin
n, m = map(int, stdin.readline().split())

l = 0
strings = []
for _ in range(n):
	s = stdin.readline()[:-1]
	strings.append(s)
	l += len(s)

x, y = (m-l) // (n-1), (m-l) % (n-1)

answer = strings[0]
for i in range(1, n):
	if((ord(strings[i][0]) >= 97 and y > 0) or (n-i <= y)):
		answer += '_'
		y -= 1
	answer += '_' * x
	answer += strings[i]

print(answer)