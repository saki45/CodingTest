# given a set of N boxes with width, height and depth. One box could be placed on top of the other only when its with, height and depth are all smaller than the other box. Find the highest possible stacks of boxes

# In this problem a box is represented as a triplet, (w, h, d)

import random

def isSmaller(box1, box2):
	# returns true if box1 is smaller than box2
	return (box1[0]<=box2[0]) and (box1[1]<=box2[1]) and (box1[2]<=box2[2])

def getRandBox(M):
	# generate a box with random height, width and depth no larger than M
	w = int(random.uniform(1, M))
	h = int(random.uniform(1, M))
	d = int(random.uniform(1, M))
	return (w, h, d)

def printBoxes(prevBox, cur, boxes):
	# print the boxes
	if cur == -1:
		return

	# print previous boxes
	printBoxes(prevBox, prevBox[cur], boxes)
	print(boxes[cur])

def calculateMaxHeight(boxes):
	N = len(boxes)
	curMaxHeight = [1 for i in range(0, N)]
	prevBox = [-1 for i in range(0, N)]

	curMaxHeight[0] = 1

	# calculate the maximum height from the first box to the cur-th box
	cur = 1
	while cur < N:
		prev = 0
		while prev < cur:
			# the prev-th box could be put on top of the cur-th box
			if isSmaller(boxes[prev], boxes[cur]):
				if curMaxHeight[cur] < curMaxHeight[prev]+1:
					curMaxHeight[cur] = curMaxHeight[prev]+ 1
					prevBox[cur] = prev
			prev += 1
		cur += 1

	# find the box with the maximum height
	highest, highestBox = 0, 0
	cur = 0
	while cur < N:
		if curMaxHeight[cur] > highest:
			highest = curMaxHeight[cur]
			highestBox = cur
		cur += 1

	# print the highest stack of boxes from top to bottom
	print(highest)
	printBoxes(prevBox, highestBox, boxes)

if __name__ == "__main__":

	# generate N boxes with random width, height and width
	N = 12
	M = 10
	boxes = [getRandBox(M) for i in range(0, N)]

	# sort boxes according to its width
	boxes.sort()
	print(boxes)

	calculateMaxHeight(boxes)
