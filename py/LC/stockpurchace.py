def findmaxdiff(a):

	N = len(a)
	cur_min, max_diff,cur_max, g_max = 999999,-99999,-1,-1

	i = N-1
	while i >= 0:
		if a[i]>cur_max:
			cur_max = a[i]
		if cur_max-a[i] > max_diff:
			max_diff = cur_max - a[i]
			cur_min = a[i]
			g_max = cur_max
		i -= 1
	print(cur_min, g_max)

if __name__ == '__main__':

	N = 15
	import random
	a = [int(random.uniform(0,2*N)) for i in range(0,N)]
	print(a)
	findmaxdiff(a)
