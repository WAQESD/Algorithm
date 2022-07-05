import sys 
input = sys.stdin.readline

n = int(input())
cases = [0] + list(map(int, input().split()))
lis = [-1000000001]
cache = [0] * (n+1)
for i in range(1, n+1):
	case = cases[i]
	if lis[-1]<case: 
		lis.append(case)
		cache[i] = len(lis) - 1
	else:
		left = 0
		right = len(lis)
		while left<right:
			mid = (right+left)//2
			if lis[mid]<case:
				left = mid+1
			else:
				right = mid
		lis[right] = case
		cache[i] = right

answer = []
maxlen = len(lis) - 1
print(maxlen)
for i in range(n, 0, -1):
	if(cache[i] == maxlen):
		answer.append(cases[i])
		maxlen -= 1
answer.reverse()
print(*answer)

"""
1
-144
13
-5 47 -1 10 20 40 10 30 -13 40 20 49 50
10
49 50 100 150 10 11 12 5 6 7 
6
11 12 50 51 52 13 14 15

"""