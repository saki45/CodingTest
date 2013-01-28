def DiceAnal(N):
	pdf = [[0 for i in range(0, 6*N+1)] for j in range(0, N+1)]
	calcPdf(pdf)

	cdf = calcCdf(pdf)

	p = [[0 for i in range(0, N+1)] for j in range(0, N+1)]
	#p[i][j] -- the probability for i dices to beat j dices
	i = 1
	while i <= N:
		j = 1
		print("Calculate attacker: ", i)
		while j <= i:
			p[i][j] = calcBeatP(pdf, cdf, i, j)
			if i != j:
				p[j][i] = 100 - p[i][j]
			j += 1
		i += 1

	for i in p:
		print(i)

def calcPdf(a):
	N = len(a) - 1
	a[1][1:7] = [1]*6
	for i in range(2,N+1):
		print(i, ":Calculate pdf", end='')
		j = i
		while j<=6*i:
			k = 1
			if j%6 == 0:
				print('.',end='')
			while k < j:
				a[i][j] += a[i-1][k]*a[1][j-k]
				k += 1
			j += 1
		print()

def calcCdf(pdf):
	N = len(pdf) - 1
	cdf = [[0 for i in range(0, 6*N+1)] for j in range(0, N+1)]
	i = 1
	while i <= N:
		print(i, ":Calculate cdf",end='')
		j = 1
		while j <= 6*N:
			cdf[i][j] = cdf[i][j-1] + pdf[i][j]
			j += 1
			if j%6 == 0:
				print('.', end='')
		i += 1
		print()
	return cdf

# m dices beat n dices (m >= n)
def calcBeatP(pdf, cdf, m, n):
	i, p = m, 0
	while i <= 6*m:
		p += pdf[m][i] * cdf[n][i-1]
		i += 1
	p = (p / 6**(m+n)) * 100
	return p


if __name__ == '__main__':

	DiceAnal(8)
