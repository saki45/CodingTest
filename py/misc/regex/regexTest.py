import re
p = re.compile('\d{3}')

with open('test.txt') as f:
	for s in f:
		print(s, end='')
		m = p.findall(s)
		for mm in m:
			print(mm)
