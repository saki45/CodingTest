a = list(range(0, 12))

import random
i = 0

while i < len(a):
	p = int(random.uniform(i, len(a)))
	tmp = a[i]
	a[i] = a[p]
	a[p] = tmp
	i += 1

for i in a:
	print(i, end = ' ')
print()
