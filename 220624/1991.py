from sys import stdin

n = int(stdin.readline())
dict = {}
for i in range(n):
	[p, l, r] = list(map(str, stdin.readline().split()))
	dict[p] = [l, r]

def pre(now, s):
	if(now == '.'): return s
	s += now
	s = pre(dict[now][0], s)
	s = pre(dict[now][1], s)
	return s

def inord(now, s):
	if(now == '.'): return s
	s = inord(dict[now][0], s)
	s += now
	s = inord(dict[now][1], s)
	return s

def post(now, s):
	if(now == '.'): return s
	s = post(dict[now][0], s)
	s = post(dict[now][1], s)
	s += now
	return s

print(pre('A', ''))
print(inord('A', ''))
print(post('A', ''))