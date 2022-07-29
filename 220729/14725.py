from sys import stdin
class Trie:
	def __init__(self, s):
		self.s = s
		self.children = {}
	
	def add(self, arr):
		if(not len(arr)): return
		if(arr[0] not in self.children.keys()): self.children[arr[0]] = Trie(arr[0])
		self.children[arr[0]].add(arr[1:])

	def show(self, depth):
		if(depth):print('--' * (depth-1) + self.s)
		for key in sorted(self.children.keys()):
			self.children[key].show(depth+1)

n = int(stdin.readline())	
T = Trie('')
for i in range(n):
	line = list(stdin.readline().split())[1:]
	T.add(line)
T.show(0)
