import collections

list = []

with open('./datafile.dat', 'rt') as infile:
	lines = infile.read().split('\n')
	for x in range(len(lines) - 1):
		num = int(lines[x])
		list.append(num)

with open('./new1.dat', 'rt') as infile:
	print("OPENED: new1.dat")
	lines = infile.read().split('\n')
	for x in range(len(lines) - 1):
		num = int(lines[x])
		list.append(num)

with open('./new2.dat', 'rt') as infile:
	print("OPENED: new2.dat")
	lines2 = infile.read().split('\n')
	for x in range(len(lines2) - 1):
		num = int(lines2[x])
		list.append(num)

with open('./new3.dat', 'rt') as infile:
	print("OPENED: new3.dat")
	lines3 = infile.read().split('\n')
	for x in range(len(lines3) - 1):
		num = int(lines3[x])
		list.append(num)

list.sort()
open('./datafile.dat', 'w').close()

for x in range(len(list)):
	inp = str(list[x])
	open('./datafile.dat', 'a').write(inp + '\n')

open('./datafile.dat', 'a').close()