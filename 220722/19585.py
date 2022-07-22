from sys import stdin
color = [set() for _ in range(2001)]
nickname = [set() for _ in range(2001)]
c, n = map(int, stdin.readline().split())
for i in range(c):
	s = stdin.readline()[:-1]
	color[len(s)].add(s)

for i in range(n):
	s = stdin.readline()[:-1]
	nickname[len(s)].add(s)

def legend(left, right):
	if(left not in color[len(left)]): return False
	if(right not in nickname[len(right)]): return False
	return True

q = int(stdin.readline())
for i in range(q):
	team = stdin.readline()[:-1]
	result = False
	for i in range(1, len(team)):
		if(legend(team[:i], team[i:])):
			result = True
			break
	print('Yes' if result else 'No')
