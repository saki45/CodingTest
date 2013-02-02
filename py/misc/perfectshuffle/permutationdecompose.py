def permutationdecompose(N):
	print(N)
	seed = 1
	while seed < N:
		print(seed,end=',')
		t = (seed*2)%(N+1)
		while t != seed:
			print(t,end=',')
			t = (t*2)%(N+1)
		print()
		seed = 3*seed
		

if __name__ == '__main__':

	permutationdecompose(8)
	permutationdecompose(6)
	permutationdecompose(0)
