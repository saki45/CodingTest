def mindivision(a, k):

	# the problem is to divide the array a into k parts
	# and keep the sum of each part to be minimum

	# c[i][j] = min(c[k][j-1], sum(a[k+1:i])

	N = len(a)
	c = [[0 for i in range(0, k+1)] for j in range(0, N)]
	prev = [[-1 for i in range(0, k+1)] for j in range(0, N)]

	i, c[0][0] = 1, a[0]
	while i < N:
		c[i][0] = c[i-1][0] + a[i]
		prev[i][0] = -1
		i += 1

	j = 1
	while j<=k:
		if j == 1:
			c[0][1] = a[0]
			prev[0][1] = -1
		else:
			c[j-1][j] = max(c[j-1][j-1], a[j-1])
			prev[j-1][j] = j-1
		i = j
		while i < N:
			c[i][j]
			l, ml, mp = j-1,99999999,0
			while l < i:
				tmp = max(c[l][j-1],  c[i][0] - c[l][0])
				if tmp < ml:
					ml = tmp
					prev[i][j] = l
				l += 1
			c[i][j] = ml
			i += 1
		j += 1

	for i in c:
		print(i)
	print()
	for i in prev:
		print(i)

	printResult(a, prev, N-1, k)

def printResult(a, prev, idx, k):
	
	lastidx = prev[idx][k]
	if lastidx != -1:
		printResult(a, prev, lastidx, k-1)
	print(a[lastidx+1:idx+1])

if __name__ == '__main__':

	a = list(range(1, 15))
	mindivision(a, 3)
