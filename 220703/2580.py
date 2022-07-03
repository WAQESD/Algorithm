from sys import stdin
sudoku = []
stack = []
for i in range(9): sudoku.append(list(map(int, stdin.readline().split())))

def check(x, y, v):
	for i in range(9):
		if(sudoku[y][i] == v): return False
		if(sudoku[i][x] == v): return False
	sectionX = 3 * (x // 3)
	sectionY = 3 * (y // 3)
	for i in range(3):
		for j in range(3):
			if(sudoku[sectionY+i][sectionX+j]== v): return False

	return True

for i in range(9):
	for j in range(9):
		if(sudoku[i][j] == 0): stack.append([i, j])

def dfs(idx):
	if (idx == len(stack)):
		for i in range(9): print(*sudoku[i])
		exit(0)
	
	for i in range(1, 10):
		[y, x] = stack[idx]
		if(check(x, y, i)):
			sudoku[y][x] = i
			dfs(idx+1)
			sudoku[y][x] = 0

dfs(0)