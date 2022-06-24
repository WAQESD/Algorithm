from sys import stdin

[A, B, M] = list(map(int, stdin.readline().split()))

def mul(A, B, M):
	if(B == 1):return A % M
	result = mul(A, B//2, M)
	if(B % 2 == 0):
		return (result * result) % M
	else:
		return (result * result * A) % M

print(mul(A, B, M))