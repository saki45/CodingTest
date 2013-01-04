a = list(range(1,20))
a.remove(8)

uni = 0

for i in range(1,20):
	uni ^= i

for i in a:
	uni ^= i

print(uni)
