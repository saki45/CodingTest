def selection(n):
	# this method print all the possible selection of number 1 to n
	if n<=0:
		return

	res = []
	selectionrecur(res, 1, n)

def selectionrecur(res, cur, n):
	if cur == n:
		res.append(n)
		print(res)
		res.pop()
		print(res)
		return

	res.append(cur)
	selectionrecur(res, cur+1, n)
	res.pop()
	selectionrecur(res, cur+1, n)

if __name__ == '__main__':

	selection(4)
