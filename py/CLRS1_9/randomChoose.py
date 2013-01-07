a = list(range(0, 12))
m = 4

import random
i = 0
S = []
while i<m:
	p = int(random.uniform(0, len(a)-i))
	if p in S:
		S.append(len(a)-1-i)
	else:
		S.append(p)
	i += 1

for i in S:
	print(i, end=' ')
print()
