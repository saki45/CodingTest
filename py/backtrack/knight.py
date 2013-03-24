
def knightPath(board, xMove, yMove, cx, cy, count):

	print(cx, cy, count)
	board[cx][cy] = count
	if count == 64:
		for row in board:
			print(row)
		return

	for i in range(0,8):
		nextX = cx + xMove[i]
		nextY = cy + yMove[i]
		if 0 <= nextX <= 7 and 0 <= nextY <= 7 and board[nextX][nextY] == 0:
			knightPath(board, xMove, yMove, nextX, nextY, count+1)

	board[cx][cy] = 0

if __name__ == '__main__':

	# Set the initial board and 8 possible moves
	board = [[0 for i in range(0,8)] for j in range(0,8)]
	xMove = [2,  2, 1, -1, -2, -2, -1, 1]
	yMove = [1, -1,-2, -2, -1,  1,  2, 2] 

	# find the path to cover the whole board, start from (0,0)
	knightPath(board, xMove, yMove, 0, 0, 1)
