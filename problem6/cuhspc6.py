line1 = input()
line2 = input().split()

n = int(line1)
p = [int(elem)-1 for elem in line2]

init_seats = [i for i in range(n)]

for i in range(n * n):
	new_seats = [None] * n
	for j in range(n): 
		if (new_seats[p[j]] is None):
			new_seats[p[j]] = init_seats[j]
		elif (init_seats[j] is not None):
			if (init_seats[j] < new_seats[p[j]]):
				new_seats[p[j]] = init_seats[j]
	init_seats = new_seats

print(sum([True if x is not None else False for x in init_seats]))
