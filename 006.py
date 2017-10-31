s = 0
sq = []
for i in range(1, 101):
	sq.append(i)
	s += i**2
print sum(sq)**2 - s
