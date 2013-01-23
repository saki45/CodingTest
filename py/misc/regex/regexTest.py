import re

p = re.compile('\d{3}')

f = open('test.txt')

for s in f:
	print(s, end='')
	m = p.findall(s)
	for mm in m:
		print(mm)

f.close()
