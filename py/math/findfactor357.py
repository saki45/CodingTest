def findfactor(N):
	# this method will print the first N numbers containing only factors of 3, 5 or 7

	# create three queues, the first one (Q3) only contains numbers with factors only 3, the second queue (Q5)
	# contains numbers with factors 3 and 5. The last queue (Q7) contains numbers with factors 3, 5, 7
	from collections import deque
	Q3, Q5, Q7 = deque([3]), deque([5]), deque([7])

	numCount = 0
	
	while numCount <= N:
		# each time we get the minimum number from the first elements in Q3, Q5 and Q7

		# if the minimum number is in Q3, then we add three corresponding numbers to Q3, Q5 and Q7
		if Q3[0]<Q5[0] and Q3[0]<Q7[0]:
			thisnum = Q3.popleft()
			print(thisnum, end=' ')
			Q3.append(thisnum*3)
			Q5.append(thisnum*5)
			Q7.append(thisnum*7)
		# if the minimum number is in Q5, then we add two numbers to Q5 and Q7
		elif Q5[0]<Q3[0] and Q5[0]<Q7[0]:
			thisnum = Q5.popleft()
			print(thisnum, end=' ')
			Q5.append(thisnum*5)
			Q7.append(thisnum*7)
		else:
			thisnum = Q7.popleft()
			print(thisnum, end=' ')
			Q7.append(thisnum*7)

		numCount += 1
	print()

if __name__ == '__main__':

	findfactor(12)

