def nearestgreater(arr):

	if len(arr) <= 1:
		return

	# This method finds the nearest greater element for a given array
	# If no NGE exists, then the result is -1
	
	N = len(arr)
	result = [-1 for i in range(0, N)]

	# use a stack to hold temorary small elements, stored in tuple (index, value)
	stack = []

	for cur in range(0, N):
		# arr[cur] is the NGE for all the elements in stack smaller than arr[cur]
		# remove all elements in the stack smaller than arr[cur], and push arr[cur] in the stack

		while len(stack)>0 and stack[len(stack)-1][1]<arr[cur]:
			idx, value = stack.pop()
			result[idx] = arr[cur]

		
		# if the stack is empty, or all the remaining elements in the stack is larger than the arr[cur]
		# then we just push arr[cur] into it
		stack.append((cur, arr[cur]))
		
	print(result)

if __name__ == '__main__':

	N = 10
	import random
	arr = [int(random.uniform(0, N*2)) for i in range(0, N)]

	print(arr)
	nearestgreater(arr)
