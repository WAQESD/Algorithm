from sys import stdin

from regex import S

n = int(stdin.readline())

inord = list(map(int, stdin.readline().split()))
post = list(map(int, stdin.readline().split()))

def tree(is_, ie, ps, pe, s):
	root = post[pe]
	print(root)
	idx = inord.index(root)
	lis = is_
	lie = idx - 1
	ris = idx + 1
	rie = ie
	lps = ps
	lpe = idx
	rps = idx+1
	rpe = pe - 1
	s += str(root) + ' '
	if(lie > lis): s = tree(lis, lie, lps, lpe, s)
	if(rpe > rps): s = tree(ris, rie, rps, rpe, s)
	return s

print(tree(0, n-1, 0, n-1 ,'')[:-1])

"""
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15

15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
"""