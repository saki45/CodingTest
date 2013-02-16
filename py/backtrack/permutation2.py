def preprocess(elements, maxElement):

	count = [0 for i in range(maxElement)]

	# count the appearance for each elements
	for cur in elements:
		count[cur] += 1

	return count

def printpermutation(elements):
	# print the elements in number form (suppose all the numbers are smaller than 10
	for ele in elements:
		print(ele,end='')
	print()

def permutation2Wrapper(elements, maxElement):

	# if all the elements are 0
	if maxElement == 1:
		printpermutation(elements)
		return

	# this method prints all the permutation in the list of given elements
	# the different is that now 'elements' contains duplicate element

	# first we count the number of appearances of each element. for simplicity we assume the elements are in
	# the range of 0...maxElement-1
	count = preprocess(elements, maxElement)

	# start from each element
	selected = []
	for i in range(0, maxElement):
		permutation2(count, selected, i)

def permutation2(count, selected, cur):

	maxElement = len(count)

	# first check whether there are other elements 
	hasOther = False
	tmp = 0
	while tmp<len(count):
		if tmp != cur and count[tmp]>0:
			hasOther = True
			break
		tmp += 1

	# if other elements exists, then we pick different number of current elements, and continue
	if hasOther:
		curCount = count[cur]
		
		while count[cur]>0:
			count[cur] -= 1
			selected.append(cur)

			# selected valid next element to continue
			for nxt in range(0, maxElement):
				if nxt != cur and count[nxt]>0:
					permutation2(count, selected, nxt)

		# remove the selected elements
		while count[cur] < curCount:
			count[cur] += 1
			selected.pop()
	else:
	# if no other elements, we just add all the remaining current element, and output the result
		curCount = count[cur]

		selected += [cur]*curCount
		printpermutation(selected)

		# remove the elements
		while curCount > 0:
			curCount -= 1
			selected.pop()

if __name__ == '__main__':

	maxElement = 3
	N = 6

	import random
	elements = [int(random.uniform(0, maxElement)) for i in range(0, N)]
	elements.sort()
	print(elements)
	permutation2Wrapper(elements, maxElement)
