def ctrlACV(N):
	if N <= 3:
		print(N)
		return
	# c[0] is unused
	c = [0 for i in range(0, N+1)]
	c[1:4] = [i for i in range(1,4)]

	for i in range(4, N+1):
		c[i] = max(c[i-1]+1, c[i])
		d = c[i-3]
		for j in range(i, N+1):
			c[j] = max(c[j], (j-i+1)*d)

	print(c)
	

if __name__ == '__main__':

	ctrlACV(10)
	print()
	ctrlACV(25)
