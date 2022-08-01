from sys import stdin
d, p, q = map(int, stdin.readline().split())
p, q = min(p, q), max(p, q)
if(d % p == 0 or d % q == 0): print(d)
else:
	result = d//q * q + q
	cnt = 0
	while(cnt < d//q+2 and cnt < q+1):
		mulq = cnt * q
		cnt += 1
		tmp = d - mulq
		if(tmp < 0): break
		if(tmp % p == 0): 
			result = d
			break
		tmp += p - (tmp % p)
		result = min(result, tmp + mulq)
	print(result)