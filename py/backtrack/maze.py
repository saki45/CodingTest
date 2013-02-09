def solvemaze(maze, x, y):
	# This method is the classic way to find the route to the exit of a maze by backtrack
	# In this program by default the exit is in the upper right corner (maze(0,8))

	# The elements in the maze:
	# 0 -- unvisited
	# 1 -- wall
	# 2 -- visited

	maze[x][y] = 2

	# find one solution
	if x==0 and y==8:
		print("solution: ")
		printmaze(maze)
		return

	# check how many options we have at the current point to reduce the number of status created
	numOfOption = 0
	isUp, isDown, isLeft, isRight = False, False, False, False	

	if x>0 and maze[x-1][y]==0:
		isUp = True
		upNo = numOfOption
		numOfOption += 1
	if x<len(maze)-1 and maze[x+1][y]==0:
		isDown = True
		downNo = numOfOption
		numOfOption += 1
	if y>0 and maze[x][y-1]==0:
		isLeft = True
		leftNo = numOfOption
		numOfOption += 1
	if y<len(maze[0])-1 and maze[x][y+1]==0:
		isRight = True
		rightNo = numOfOption
		numOfOption += 1

	if numOfOption == 0:
		return

	status = [copy.deepcopy(maze) for i in range(1,numOfOption)]
	status = [maze] + status

	if isUp:
		solvemaze(status[upNo],x-1,y)
	if isDown:
		solvemaze(status[downNo],x+1,y)
	if isLeft:
		solvemaze(status[leftNo],x,y-1)
	if isRight:
		solvemaze(status[rightNo],x,y+1)
		
	

def printmaze(maze):

	for row in maze:
		for n in row:
			print(n, end=' ')
		print()

if __name__ == "__main__":

	import copy
	maze = [[0 for i in range(0,9)] for j in range(0,9)]

	maze[1][1:8] = [1 for i in range(1,8)]
	maze[3][0:7] = [1 for i in range(0,7)]
	maze[3][8] = 1
	maze[4][4] = 1
	maze[5][0] = 1
	maze[5][2:6] = [1 for i in range(2,6)]
	maze[5][7:9] = [1, 1]
	maze[7][0:5] = [1 for i in range(0,5)]
	maze[7][6:9] = [1 for i in range(6,9)]

	printmaze(maze)
	
	maze[3][3] = 0
	maze[8][0] = 2
	solvemaze(maze,8,0)
