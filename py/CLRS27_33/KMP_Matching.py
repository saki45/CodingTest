def KMPMatch(T, P):

	T = list(T)
	P = list(P)
	Pi = KMPPreprocess(P)

	j = -1
	for i in range(0, len(T)):
		while j>=0 and T[i] != P[j+1]:
			j = Pi[j]
		if T[i] == P[j+1]:
			j += 1
			if j == len(P)-1:
				print(i-len(P)+1)
				j = Pi[j]
		

def KMPPreprocess(P):

	l = len(P)
	Pi = [-1 for i in range(0, l)]
	j = -1
	for i in range(2, l):
		while j >= 0 and P[i] != P[j+1]:
			j = Pi[j]

		if P[i] == P[j+1]:
			j += 1
		Pi[i] = j

	return Pi


if __name__ == '__main__':

	T = 'bacbabababacabab'
	P = 'abab'

	print(T)
	print(P)
	KMPMatch(T, P)
