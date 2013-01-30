def floodfillRecursive(a, i, j, N, serial):

	# invalid cases

	# (1) out of bound
	if i<0 or i>=N or j<0 or j>=N:
		return serial
	# (2) already visited or wall
	if a[i][j] != 0:
		return serial

	a[i][j] = serial
	serial = serial + 1

	# search for 4 directions
	serial = floodfillRecursive(a, i-1, j, N, serial)
	serial = floodfillRecursive(a, i, j-1, N, serial)
	serial = floodfillRecursive(a, i+1, j, N, serial)
	serial = floodfillRecursive(a, i, j+1, N, serial)
	return serial

def floodfillQueue(a, m, n, N):

	# This version of implementation uses a deque
	
	if not (0<=m<N and 0<=n<N):
		return
	if a[m][n]!=0:
		return

	q = []
	from collections import deque
	q = deque(q)
	serial = 1

	# floodfill starts at (m, n)

	q.append((m,n))
	while len(q)>0:
		i, j = q.popleft()
		if 0<=i<N and 0<=j<N:
			if a[i][j] == 0:
				a[i][j] = serial
				serial += 1
				q.append((i-1, j))
				q.append((i, j-1))
				q.append((i+1, j))
				q.append((i, j+1))

def floodfillStack(a, m, n, N):

	# flood fill with stack
	
	if not (0<=m<N and 0<=n<N):
		return
	if a[m][n]!=0:
		return

	st = []
	st.append((m, n))
	serial = 1
	while len(st)>0:
		i, j = st.pop()
		if 0<=i<N and 0<=j<N:
			if a[i][j] == 0:
				a[i][j] = serial
				serial += 1
				st.append((i-1, j))
				st.append((i, j-1))
				st.append((i+1, j))
				st.append((i, j+1))
				
def printMap(a):
	for i in a:
		for j in i:
			if 0<=j<10:
				print(' ',j,' ',sep='',end='')
			else:
				print(j,' ',sep='',end='')
		print()


if __name__ == "__main__":

	N = 10
	a = [[0 for i in range(0, N)] for j in range(0, N)]

	# element value explanation:
	# 0 -- available and not visited
	# >0 - available and visited
	# -1 - wall
	
	print('\n----------- Recursive -------------\n')
	floodfillRecursive(a, N//2, N//2, N, 1);
	printMap(a)

	print('\n------ Recursive with bound -------\n')
	b = [[0 for i in range(0, N)] for j in range(0, N)]
	b[3][2:] = [-1]*(N-2)
	floodfillRecursive(b, N//2, N//2, N, 1);
	printMap(b)

	c = [[0 for i in range(0, N)] for j in range(0, N)]
	print('\n------------ Queue ----------------\n')
	floodfillQueue(c, N//2, N//2, N)
	printMap(c)

	d = [[0 for i in range(0, N)] for j in range(0, N)]
	print('\n------- Queue with Bound ----------\n')
	d[3][2:] = [-1]*(N-2)
	floodfillQueue(d, N//2, N//2, N)
	printMap(d)

	e = [[0 for i in range(0, N)] for j in range(0, N)]
	print('\n------------ Stack ----------------\n')
	floodfillStack(e, N//2, N//2, N)
	printMap(e)

	f = [[0 for i in range(0, N)] for j in range(0, N)]
	print('\n------- Stack with Bound ----------\n')
	f[3][2:] = [-1]*(N-2)
	floodfillStack(f, N//2, N//2, N)
	printMap(f)
