from sys import stdin
import math
n, t = map(int, stdin.readline().split())
arr = [0] + list(map(int, stdin.readline().split()))
cnt = [0] * 1000001
sqrtN = int(math.sqrt(n))
query = []
answer = [0] * t
for i in range(t):
	s, e = map(int, stdin.readline().split())
	query.append([s // sqrtN, e, s, i])
query.sort()
def add(v):
	cnt[v] += 1
	return (2*cnt[v]-1) * v

def remove(v):
	cnt[v] -= 1
	return (2*cnt[v]+1) * v

left = 0
right = 0
result = 0
for [_, e, s, i] in query:
	while(left > s):
		left -= 1
		result += add(arr[left])
	while(left < s): 
		result -= remove(arr[left])
		left += 1
	while(right > e):
		result -= remove(arr[right])
		right -= 1
	while(right < e): 
		right += 1
		result += add(arr[right])
	answer[i] = result

for ans in answer: print(ans)
