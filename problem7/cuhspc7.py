line = [int(ele) for ele in input().split()]

cell = line[0]
neighbors = sum(line[1:])

if (cell == 1): 
	if (neighbors < 2 or neighbors > 3): 
		cell = 0
else: 
	if (neighbors == 3):
		cell = 1

print(cell)
