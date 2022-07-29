from sys import stdin
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
A.sort()
B.sort()
a = [A[i] - A[i-1] for i in range(1, n)] + [360000 - A[-1] + A[0]]
b = [B[i] - B[i-1] for i in range(1, n)] + [360000 - B[-1] + B[0]]
a = a + a
def getPartialMatch(b):
	pi = [0] * n
	begin = 1
	matched = 0
	while(begin + matched < n):
		if(b[begin + matched] == b[matched]):
			matched += 1
			pi[begin + matched -1] = matched
		else:
			if(matched == 0): begin += 1
			else:
				begin += matched - pi[matched-1]
				matched = pi[matched-1]
	return pi

def kmp(a, b):
	pi = getPartialMatch(b)
	answer = False
	begin = 0
	matched = 0
	while(begin <= n):
		if(matched < n and a[begin+matched] == b[matched]):
			matched += 1
			if(matched == n):
				answer = True
				break
		else:
			if(matched == 0): begin += 1
			else:
				begin += matched - pi[matched-1]
				matched = pi[matched-1]

	return answer
print('possible' if kmp(a,b) else 'impossible')