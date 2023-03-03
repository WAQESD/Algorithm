from sys import stdin

n = int(stdin.readline())
sharks = []
for i in range(n):
    sharks.append(list(map(int, stdin.readline().split())))
    
canEat = [[] for _ in range(n)]
feed = [-1] * n
visit = [False] * n

for i in range(n):
    for j in range(n):
        if i == j: continue
        if sharks[i][0] < sharks[j][0] or sharks[i][1] < sharks[j][1] or sharks[i][2] < sharks[j][2]: continue
        if sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1] and sharks[i][2] == sharks[j][2] and i < j: continue
        canEat[i].append(j)


def dfs(x):
    for nxt in canEat[x]:
        if visit[nxt]: continue
        visit[nxt] = True
        if feed[nxt] == -1 or dfs(feed[nxt]):
            feed[nxt] = x
            return True
    return False

for i in range(2):
    for j in range(n):
        visit = [False] * n
        dfs(j)
        
print(feed.count(-1))