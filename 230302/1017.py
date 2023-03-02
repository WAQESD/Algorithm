from sys import stdin
from sys import exit
from math import sqrt

def isPrime(x):
	for i in range(2, int(sqrt(x))+1):
		if(x % i == 0): return False
	return True

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

odds = []
evens = []


for number in numbers:
    if(number % 2 == 0): evens.append(number)
    else: odds.append(number)
    
if(len(evens) != len(odds)):
    print(-1)
    exit()

if(numbers[0] % 2 == 0):
	[odds, evens] = [evens, odds]

matching = []
used = [0] * len(evens)
owned = [-1] * len(evens)
for odd in odds:
	tmp = []
	for i in range(len(evens)):
		even = evens[i]
		if(isPrime(odd+even)):
			tmp.append(i)
	if(len(tmp) == 0):
		print(-1)
		exit()
	matching.append(tmp)

def dfs(x):
	for even in matching[x]:
		if(used[even]): continue
		used[even] = True
		if(owned[even] == -1 or dfs(owned[even])):
			owned[even] = x
			return True
	return False

answer = []
for matched in matching[0]:
	owned = [-1] * len(evens)
	owned[matched] = 0
	cnt = 1
	for i in range(1, len(odds)):
		used = [0] * len(evens)
		used[matched] = 1
		if(dfs(i)): cnt += 1

	if(cnt == len(odds)):
		answer.append(evens[matched])

if(0 == len(answer)):
	print(-1)
else:
	answer.sort()
	for ans in answer:
		print(ans, end=" ")
