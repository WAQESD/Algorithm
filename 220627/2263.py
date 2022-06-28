from sys import stdin
import sys
sys.setrecursionlimit(10**9)

n = int(stdin.readline())

inord = list(map(int, stdin.readline().split()))
post = list(map(int, stdin.readline().split()))

position = [0]*(n+1)
for i in range(n): position[inord[i]] = i

def tree(is_, ie, ps, pe):
	if(is_ > ie or ps > pe): return
	root = post[pe]
	print(root, end= ' ')
	left = position[root] - is_
	right = ie - position[root]
	tree(is_, is_+left-1, ps, ps+left-1)
	tree(ie-right+1, ie, pe-right, pe-1)


tree(0, n-1, 0, n-1)

"""
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15

15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
"""