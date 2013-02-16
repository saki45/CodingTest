def permutation(n):
	# this method prints the permutation among number 1 to n

	if n<=0:
		return
	if n==1:
		print(1)
		return

	per = []
	used = [0 for i in range(0, n)]

	for i in range(1, n+1):
		permutationrecur(per, used, i, 0)

def permutationrecur(per, used, m, level):
	n = len(used)
	if level == n-1:
		per.append(m)
		print(per)
		per.pop()
		return

	per.append(m)
	used[m-1] = 1

	i = 0
	while i < n:
		if used[i] == 0:
			permutationrecur(per, used, i+1, level+1)
		i += 1

	per.pop()
	used[m-1] = 0

if __name__ == '__main__':

	permutation(4)
