from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def post(first, end):
	if (first > end): return
	mid = end+1
	for i in range(first+1, end+1):
		if(num_list[first] < num_list[i]):
			mid = i
			break

	post(first+1, mid-1)
	post(mid, end)
	print(num_list[first])

num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break
post(0, len(num_list)-1)
