from sys import stdin
n, m = map(int, stdin.readline().split())

emp = [[] for _ in range(n+1)]
works = [0] * (m+1)
owner = [0] * (m+1)

for i in range(1, n+1):
    emp[i] = list(map(int, stdin.readline().split()))[1:]
    
def dfs(x):
    for work in emp[x]:
        if(works[work]): continue
        works[work] = 1
        if(owner[work] == 0 or dfs(owner[work])):
            owner[work] = x
            return True
        
    return False
    
cnt = 0
for i in range(1, n+1):
    works = [0] * (m+1)
    if(dfs(i)): cnt += 1
    
print(cnt)