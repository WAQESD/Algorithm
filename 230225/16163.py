from sys import stdin

s = stdin.readline()[:-1]
n = len(s)
answer = 0

odd = [0] * n
even = [0] * n

l = 0
r = -1

for i in range(n):
    gap = 1 if i > r else min(r-i+1, odd[l+r-i])
    while(i-gap >= 0 and i+gap < n and s[i-gap] == s[i+gap]):
        gap += 1
    odd[i] = gap
    gap -= 1
    if(i+gap > r):
        l = i - gap
        r = i + gap
        
l = 0
r = -1
for i in range(n):
    gap = 0 if i > r else min(r-i+1, even[l+r-i-1])
    while(i-gap-1 >= 0 and i+gap < n and s[i-gap-1] == s[i+gap]):
        gap += 1
        
    even[i] = gap
    gap -= 1
    if(i+gap > r):
        l = i-gap-1
        r = i+gap
        
print(odd)
print(even)
print(sum(odd) + sum(even))