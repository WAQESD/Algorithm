from sys import stdin
src = stdin.readline()[:-1]
pattern = stdin.readline()[:-1]

def getPartialMatch(b):
	pi = [0] * len(b)
	begin = 1
	matched = 0
	while(begin + matched < len(b)):
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
	answer = []
	begin = 0
	matched = 0
	while(begin <= len(a) - len(b)):
		if(matched < len(b) and a[begin+matched] == b[matched]):
			matched += 1
			if(matched == len(b)):
				answer.append(begin+1)
		else:
			if(matched == 0): begin += 1
			else:
				begin += matched - pi[matched-1]
				matched = pi[matched-1]

	return answer

answer = kmp(src, pattern)
print(len(answer))
print(*answer)
