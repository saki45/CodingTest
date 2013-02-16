def findminsumWrapper(matrix):

	N = len(matrix)
	result = []
	curminresult = []
	curmin = [N*N*N]
	minimum = N*N*N
	minresult = []
	selected = [0]

	for i in range(0, N):
		findminsum(matrix, result, curminresult, 0, curmin, 0, i, N, selected)
		if curmin[0] < minimum:
			minimum = curmin[0]
			minresult = result.copy()
			print(i, result)

	print()
	print(minresult)
	print(minimum)

def findminsum(matrix, result, curminresult, cursum, curmin, row, col, N, selected):
	
	# We first examine whether the current sum after adding the element at matrix[row][col] exceeds the current minimum, if not then we add the current element to the results
	if cursum+matrix[row][col] <= curmin[0]:
		cursum += matrix[row][col]
		curminresult.append(matrix[row][col])
		selected[0] |= 1<<col;

	 
		# if we already reached the last row, see whether the current result is smaller than current minimum
		if row == N-1:
			# if so then we update the current result
			if cursum < curmin[0]:
				curmin[0] = cursum
				result = curminresult.copy()
				print(cursum, result)
		else:
			# otherwise we pick the feasible elements (matrix[row+1][i]) in the next row
			for i in range(0, N):
				if selected[0] & (1<<i) == 0:
					findminsum(matrix, result, curminresult, cursum, curmin, row+1, i, N, selected)

		# remove the current item, and return
		curminresult.pop()
		selected[0] &= ~(1<<col)


if __name__ == "__main__":

	N = 6
	import random
	matrix = [[int(random.uniform(0, N*N)) for j in range(0, N)] for i in range(0, N)]

	for row in matrix:
		print(row)

	findminsumWrapper(matrix)
