lst = [2]
N = 100
n = 3

while n < N:
	isDiv = 0
	for div in lst:
		if(n%div == 0):
			isDiv = 1
			break
	if(isDiv == 0):
		lst.append(n)
	n = n+2

count = 0
for i in lst:
	print(i, end='\t')
	count = count + 1
	if(count % 5 == 0):
		print()



