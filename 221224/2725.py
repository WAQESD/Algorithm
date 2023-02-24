from sys import stdin
tc = int(stdin.readline())

def gcd(a, b):
	a, b = max(a, b), min(a, b)
	while(b != 0):
		a ,b = b, a % b
	return a

cases = []

for i in range(tc):
	cases.append(int(stdin.readline()))

M = max(cases)
answers = [3]

for i in range(1, M+1):
	cnt = 0
	for j in range(1, i):
		if(gcd(j, i) == 1): cnt += 1 if j == i else 2
	answers.append(answers[i-1] + cnt)

for i in cases:
	print(answers[i])