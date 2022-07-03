from sys import stdin
from itertools import combinations
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr1 = arr[:n//2]
arr2 = arr[n//2:]

sum1 = []
sum2 = []

for i in range(len(arr1) + 1):
	combs = combinations(arr1, i)
	for comb in combs:
		sum1.append(sum(comb))
sum1.sort()
for i in range(len(arr2) + 1):
	combs = combinations(arr2, i)
	for comb in combs:
		sum2.append(sum(comb))
sum2.sort()

left = 0
right = len(sum2)-1
result = 0

while (left < len(sum1) and right >= 0):
	l = sum1[left]
	r = sum2[right]
	v = l + r
	if(v < s): left += 1
	elif(v > s): right -= 1
	else:
		cnt1 = 1
		cnt2 = 1
		left += 1
		right -= 1
		while(left < len(sum1) and sum1[left] == l): 
			left += 1
			cnt1 += 1
			
		while(right >= 0 and sum2[right] == r):
			right -= 1
			cnt2 += 1

		result += cnt1 * cnt2

if(s == 0): result -= 1
print(result)