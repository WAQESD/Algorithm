from sys import stdin
from collections import deque
sudoku = []
for i in range(9): sudoku.append(list(map(int, stdin.readline().split())))

def candi(x, y):
	tmp = [0] + [1] * 9
	for i in range(9):
		tmp[sudoku[y][i]] = 0
	for i in range(9):
		tmp[sudoku[i][x]] = 0
	sectionX = 3 * (x // 3)
	sectionY = 3 * (y // 3)
	for i in range(3):
		for j in range(3):
			tmp[sudoku[sectionY+i][sectionX+j]] = 0
	cand = []
	for i in range(1,10): 
		if(tmp[i] == 1): cand.append(i)
	return cand 

q = deque()
for i in range(9):
	for j in range(9):
		if(sudoku[i][j] > 0): continue
		cand = candi(j, i)
		if(len(cand) == 1): sudoku[i][j] = cand[0]
		else: q.append([i, j])

while(len(q)):
	[i, j] = q.popleft()
	cand = candi(j, i)
	if(len(cand) == 1): sudoku[i][j] = cand[0]
	else: q.append([i, j])

for i in range(9):
	print(*sudoku[i])
