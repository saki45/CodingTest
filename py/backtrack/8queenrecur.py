global solutionCount
solutionCount = 0

def eightqueenrecur(cx, cy, row, col, ul, ur, st):
	# This is an recursive implementation of 8queen problem
	# in this implementation I use 4 bit maps to quickly detect whether a queen position is valid

	global solutionCount

	isValid = (row & (1<<cx)) + (col & (1<<cy)) + (ul & (1<<(7-cx+cy))) + (ur & (1<<(cx+cy)))

	if isValid == 0:
		if len(st) == 7:
			solutionCount += 1
			st.append((cx, cy))
			printResult(solutionCount, st)
			st.pop()
			return

		# if the queen is in (cx, cy), then
		# The cx-th row is labelled
		row |= 1 << cx
		# The cy-th column is labelled
		col |= 1 << cy
		# The (7-cx+cy)-th upperLeft - lowerRight diagnol line is labelled
		ul |= 1 << (7-cx+cy)
		# The (cx+cy)-th lowerLeft - upperRight diagnol line is labelled
		ur |= 1 << (cx+cy)

		st.append((cx, cy))

		ncx, ncy = cx+1, 0
		while ncy<8:
			eightqueenrecur(ncx, ncy, row, col, ul, ur, st)
			ncy += 1

		st.pop()
		row &= ~(1<<cx)
		col &= ~(1<<cy)
		ul &= ~(1<<(7-cx+cy))
		ur &= ~(1<<(cx+cy))

def printResult(solutionCount, st):
	print("Solution ",solutionCount,sep='')
	print(st)
	for pts in st:
		q = pts[1]
		for i in range(0,8):
			if i == q:
				print('o',end='')
			else:
				print('-',end='')
		print()

if __name__ == '__main__':
	for i in range(0,8):
		eightqueenrecur(0, i, 0, 0, 0, 0, [])
