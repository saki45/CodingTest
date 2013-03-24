def simpleNearestPair(points):
	i = 0
	minDist = 999
	point1 = 0
	point2 = 0

	while i < len(points)-1:
		j = i+1
		while j < len(points):
			dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
			if dist < minDist:
				minDist = dist
				point1 = points[i]
				point2 = points[j]
			j += 1
		i += 1

	minDist = minDist ** 0.5

	print("minimum distance is ", minDist, sep='')
	print("Nearest pair is ", point1, " and ", point2, sep='')

def getDistance(point1, point2):

	dist = (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
	return dist

def nearestPair(points):

	points.sort()
	print(points)
	point1, point2, minDist = nearestPairUtil(points, 0, len(points)-1)
	minDist = minDist ** 0.5
	print("minimum distance is ", minDist, sep='')
	print("Nearest pair is ", point1, " and ", point2, sep='')

def nearestPairUtil(points, st, ed):

	if st == ed:
		return points[st], points[ed], -1

	mid = (st+ed) // 2
	pL1, pL2, distL = nearestPairUtil(points, st, mid)
	pR1, pR2, distR = nearestPairUtil(points, mid+1, ed)

	if distL == -1 and distR == -1:
		dist = getDistance(pL1, pR1)
		return pL1, pR1, dist
	elif distL == -1:
		kdd, distLR, pM1, pM2 = mid+1, 999, pL1, pL2
		while kdd <= ed:
			dist = getDistance(pL1, points[kdd])
			if dist < distLR:
				distLR = dist
				pM2 = points[kdd]
			kdd += 1
		if distLR < distR:
			return pM1, pM2, distLR
		else:
			return pR1, pR2, distR
	elif distR == -1:
		kdd, distLR, pM1, pM2 = mid, 999, pR1, pR2
		while kdd >= st:
			dist = getDistance(points[kdd], pR1)
			if dist < distLR:
				distLR = dist
				pM1 = points[kdd]
			kdd -= 1
		if distLR < distL:
			return pM1, pM2, distLR
		else:
			return pL1, pL2, distL
	else:
		minDistLR = (min(distL, distR)) ** 0.5
		midLine = (points[mid][0] + points[mid+1][0])/2
		idxL = mid
		while idxL >= st and points[idxL][0] + minDistLR >= midLine:
			idxL -= 1
		idxR = mid+1
		while idxR <= ed and points[idxR][0] - minDistLR <= midLine:
			idxR += 1

		if idxL == mid or idxR == mid+1:
			if distL < distR:
				return pL1, pL2, distL
			else:
				return pR1, pR2, distR

		idxL, idxR = idxL+1, idxR-1

		tmpL = sorted(points[idxL:mid+1], key = lambda x:x[1])
		tmpR = sorted(points[mid+1:idxR+1], key = lambda x:x[1])
		
		idxL, idxR, distLR, pM1, pM2 = 0, 0, 999, tmpL[0], tmpR[0]
		dist = getDistance(tmpL[0], tmpR[0])
		while idxL < len(tmpL)-1 and idxR < len(tmpR)-1:
			if dist < distLR:
				distLR = dist
				pM1, pM2 = tmpL[idxL], tmpR[idxR]

			ndistL = getDistance(tmpL[idxL+1], tmpR[idxR])
			ndistR = getDistance(tmpL[idxL], tmpR[idxR+1])

			if ndistL < ndistR:
				dist = ndistL
				idxL += 1
			else:
				dist = ndistR
				idxR += 1

		if idxL == len(tmpL)-1:
			while idxR < len(tmpR):
				dist = getDistance(tmpL[idxL], tmpR[idxR])
				if dist < distLR:
					distLR = dist
					pM1, pM2 = tmpL[idxL], tmpR[idxR]
				idxR += 1

		if idxR == len(tmpR)-1:
			while idxL < len(tmpL):
				dist = getDistance(tmpL[idxL], tmpR[idxR])
				if dist < distLR:
					distLR = dist
					pM1, pM2 = tmpL[idxL], tmpR[idxR]
				idxL += 1

		minDist = min(distL, distR, distLR)
		if minDist == distL:
			return pL1, pL2, distL
		elif minDist == distR:
			return pR1, pR2, distR
		else:
			return pM1, pM2, distLR

if __name__ == '__main__':

	from random import uniform
	N = 84
	M = 285
	points = [(int(uniform(0, M)), int(uniform(0, M))) for i in range(0, N)]
	print(points)

	simpleNearestPair(points)

	nearestPair(points)
