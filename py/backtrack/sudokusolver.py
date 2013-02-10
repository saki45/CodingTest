def preprocess(board):
	i, j = 0, 0
	flag = [[0 for i in range(0, 9)] for j in range(0, 9)]
	verti, hori, blk = [0 for i in range(0,9)], [0 for i in range(0,9)], [0 for i in range(0,9)]
	while i<9:
		j = 0
		while j<9:
			num = board[i][j]
			if num != 0:
				flag[i][j] = 1
				setstatus(num, i, j, verti, hori, blk)
			j += 1
		i += 1
	return flag, verti, hori, blk

def setstatus(num, i, j, verti, hori, blk):
	verti[j] |= 1<<num
	hori[i] |= 1<<num
	ni, nj = i//3, j//3
	blk[ni*3+nj] |= 1<<num

def clearstatus(num, i, j, verti, hori, blk):
	verti[j] &= ~(1<<num)
	hori[i] &= ~(1<<num)
	ni, nj = i//3, j//3
	blk[ni*3+nj] &= ~(1<<num)

def checkstatus(num, i, j, verti, hori, blk):
	ni, nj = i//3, j//3
	#print(i, j, verti, hori, blk)
	#print(verti[j]&(1<<num) , hori[i]&(1<<num) , blk[ni*3+nj]&(1<<num))
	#print((verti[j]&(1<<num)) +(hori[i]&(1<<num)) +(blk[ni*3+nj]&(1<<num)))
	return ((verti[j]&(1<<num)) + (hori[i]&(1<<num)) +(blk[ni*3+nj]&(1<<num))) == 0

def sudokusolve(board, flag, i, j, verti, hori, blk):
	if j == 9:
		if i == 8:
			print()
			for row in board:
				print(row)
			return
		sudokusolve(board, flag, i+1, 0, verti, hori, blk)
		return

	if flag[i][j] == 1:
		sudokusolve(board, flag, i, j+1, verti, hori, blk)
		return

	for n in range(1, 10):
		#print(i,j,n, checkstatus(n, i, j, verti, hori, blk))
		#input()
		if checkstatus(n, i, j, verti, hori, blk):
			setstatus(n, i, j, verti, hori, blk)
			board[i][j] = n
			sudokusolve(board, flag, i, j+1, verti, hori, blk)
			clearstatus(n, i, j, verti, hori, blk)
			board[i][j] = 0	

if __name__ == '__main__':

	board = [[0 for i in range(0, 9)] for j in range(0, 9)]
	board[0][2] = 3
	board[0][4] = 5
	board[0][5] = 1
	board[1][5] = 8
	board[1][6] = 7
	board[1][8] = 4
	board[2][1] = 2
	board[2][2] = 9
	board[2][7] = 3
	board[3][5] = 5
	board[3][7] = 9
	board[4][0] = 2
	board[4][8] = 3
	board[5][1] = 6
	board[5][3] = 7
	board[6][1] = 8
	board[6][6] = 3
	board[6][7] = 4
	board[7][0] = 5
	board[7][2] = 6
	board[7][3] = 8
	board[8][3] = 4
	board[8][4] = 7
	board[8][6] = 6

	for row in board:
		print(row)

	flag, verti, hori, blk = preprocess(board)
	sudokusolve(board, flag, 0, 0, verti, hori, blk)
