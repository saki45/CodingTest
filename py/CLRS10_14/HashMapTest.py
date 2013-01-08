hm = {}
hm['one'] = 1
hm['two'] = 2
hm['three'] = 3

print(hm['one'])

for i in hm.keys():
	print(i)

hm.pop('one')

for i in hm.keys():
	print(i)
