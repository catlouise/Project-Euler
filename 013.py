import sys 
l = sys.stdin.readline()
total = 0
for i in range(0,100):
	total += long(l)
	l = sys.stdin.readline()
for i in range(0, 10):
	print str(total)[i].strip(), 
  # Prints correct answer but with a space between each character
  
