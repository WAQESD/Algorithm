from sys import stdin
n = int(stdin.readline())
stack = []
answer = 0
for i in range(n):
	h = int(stdin.readline())
	while stack and stack[-1][0] < h:
		answer += stack.pop()[1]
	if not stack:
		stack.append((h, 1))
		continue
	if stack[-1][0] == h:
		cnt = stack.pop()[1]
		answer += cnt
		if stack: answer += 1
		stack.append((h, cnt+1))
	else:
		stack.append((h, 1))
		answer += 1
print(answer)

