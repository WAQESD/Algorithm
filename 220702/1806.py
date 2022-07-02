from sys import stdin
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
if(sum(arr) < s): print(0)
else:
	left = 0
	right = 0
	result = n
	l = 1
	total = arr[left]
	while(left < n):
		if(total < s):
			right += 1
			if(right >= n): break
			total += arr[right]
			l += 1
		else:
			result = min(result, l)
			if(result == 1): break
			total -= arr[left]
			l -= 1
			left += 1
	print(result)