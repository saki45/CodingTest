def findkthJoint(A, B, k):

	# find the kth largest element in two sorted arrays, A and B

	M, N = len(A), len(B)

	if M+N<k:
		return None

	if M == 0:
		return B[k-1]
	if N == 0:
		return A[k-1]
	if M+N == k:
		return max(A[M-1], B[N-1])

	sa, sb = 0,0

	while True:
		i = (int)((M-sa)/(M+N-sa-sb)*k) + sa
		j = (k-1) - (i-sa) + sb

		if (j<=sb or B[j-1]<=A[i]) and (j>=M or A[i]<=B[j]):
			return A[i]
		if (i<=sa or A[i-1]<=B[j]) and (i>=N or B[j]<=A[i]):
			return B[j]

		if A[i]<B[j-1]:
			k = k - (i+1-sa)
			sa = i + 1
		else:
			k = k - (j+1-sb)
			sb = j + 1

if __name__ == '__main__':
	import random

	M = 10
	N = 8

	A = [int(random.uniform(0, M*N)) for i in range(0, M)]
	B = [int(random.uniform(0, M*N)) for i in range(0, N)]

	A.sort()
	B.sort()

	print(A)
	print(B)

	C = A+B
	C.sort()
	
	k = 3
	print("The ",k," th element is:",sep='')
	print(C[k-1])
	print(findkthJoint(A, B, k))

	k = 11
	print("The ",k," th element is:",sep='')
	print(C[k-1])
	print(findkthJoint(A, B, k))
