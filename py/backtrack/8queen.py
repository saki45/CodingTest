def eightqueen():
	# This is an iterative implementation of 8queen problem
	# in this implementation I use 4 bit maps to quickly detect whether a queen position is valid
	st = [(0, 0)]
	cx, cy = 0, 0

	# 4 bit maps
	row, col, ul, ur = 0, 0, 0, 0

	# put the first queen in (0,0)

	# if the queen is in (cx, cy), then
	# The cx-th row is labelled
	row = row | (1 << cx)
	# The cy-th column is labelled
	col = col | (1 << cy)
	# The (7-cx+cy)-th upperLeft - lowerRight diagnol line is labelled
	ul = ul | (1 << (7-cx+cy))
	# The (cx+cy)-th lowerLeft - upperRight diagnol line is labelled
	ur = ur | (1 << (cx+cy))

	solutionCount = 0

	while len(st)>0:
		lx, ly = st[len(st)-1]
		cx, cy = lx+1, 0
		isFinished = False
		# if reach the last row, find all the possible answers
		if cx == 7:
			while cy<8:
				#print( (row & (1<<cx)) , (col & (1<<cy)) , (ul & (1<<(7-cx+cy))) , (ur & (1<<(cx+cy))))
				isValid = (row & (1<<cx)) + (col & (1<<cy)) + (ul & (1<<(7-cx+cy))) + (ur & (1<<(cx+cy)))
				#print(st,(cx, cy), isValid)
				#print(row, col, ul, ur)
				# find answer
				if isValid == 0:
					st.append((cx, cy))
					solutionCount += 1
					printResult(solutionCount,st)
					st.pop()
				cy += 1
			isFinished = True
		else:
		# check the next available position in the next line
			while cy<8 and ((row & (1<<cx)) + (col & (1<<cy)) + (ul & (1<<(7-cx+cy))) + (ur & (1<<(cx+cy))))!= 0:
				cy += 1
			
		# if we could put a queen in the next line
			if cy<8:
				#print( (row & (1<<cx)) , (col & (1<<cy)) , (ul & (1<<(7-cx+cy))) , (ur & (1<<(cx+cy))))
				st.append((cx, cy))
				row = row | (1<<cx)
				col = col | (1<<cy)
				ul = ul | (1<<(7-cx+cy))
				ur = ur | (1<<(cx+cy))
				#print(row, col, ul, ur)
				#print(st)
				#input()
			else:
				isFinished = True

		# return to previous line, choose the next position, clear the corresponding bits
		if isFinished:
			hasNoElement = True

			lx, ly = st.pop()
			row = row & ~(1<<lx)
			col = col & ~(1<<ly)
			ul = ul & ~(1<<(7-lx+ly))
			ur = ur & ~(1<<(lx+ly))
			ly += 1
			#print('pop',lx, ly)
			while hasNoElement:
				while ly<8 and ((row & (1<<lx)) + (col & (1<<ly)) + (ul & (1<<(7-lx+ly))) + (ur & (1<<(lx+ly))))!= 0:
					ly += 1
					#print('fd',lx, ly,st)
					#input()

				if ly==8 and len(st)==0:
					hasNoElement = False

				# no avalable slot in current line
				elif ly==8:
					lx, ly = st.pop()
					row = row & ~(1<<lx)
					col = col & ~(1<<ly)
					ul = ul & ~(1<<(7-lx+ly))
					ur = ur & ~(1<<(lx+ly))
					ly += 1
					#print('lf',lx, ly, st)
					#print(row, col, ul, ur)
				else:
					hasNoElement = False
					st.append((lx, ly))
					row = row | (1<<lx)
					col = col | (1<<ly)
					ul = ul | (1<<(7-lx+ly))
					ur = ur | (1<<(lx+ly))
					#print("aa",st)
					#print(row, col, ul, ur)
				

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
	eightqueen()
