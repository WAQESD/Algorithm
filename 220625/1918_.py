from sys import stdin

line = str(stdin.readline())[:-1]

def find(s):
	print(s)
	closed = 0
	op = 0
	idx = 0
	for i in range(len(s)):
		if(len(s) == 3): 
			idx = 1
			break
		idx = i
		if(s[i] == '('): closed += 1
		if(s[i] == ')'): closed -= 1
		if(closed == 0 and s[i] == '*' or s[i] == '/'): 
			if(op == 0): op = 1
			else: break
		if(closed == 0 and s[i] == '+' or s[i] == '-'): break
	
	A = s[:idx]
	if(A[0] == '('): A = A[1:-1]
	oper = s[idx]
	B = s[idx+1:]
	if(B[0] == '('): B = B[1:-1]
	return [A, oper, B]


def post(A, oper, B):
	if(len(A) > 1): 
		[a, op, b] = find(A)
		A = post(a, op, b)
	if(len(B) > 1): 
		[a, op, b] = find(B)
		B = post(a,op,b)
	return A + B + oper
[A, oper, B] = find(line)

print(post(A, oper, B))

