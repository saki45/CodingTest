import random
N = 10
a = []
n = 0
while n<N:
	a.append(int(random.uniform(4*N,1)-6*N))
	n = n+1

def printArray(a):
	for i in a:
		print(i,end=' ')
	print()

printArray(a)
cur_max, cur_idx, p = a[0],0,1
cur_sum = [0] * N
cur_pre = [0] * N
cur_sum[0] = a[0]

while p < N:
	if cur_sum[p-1] + a[p] < a[p]:
		cur_sum[p] = a[p]
		cur_pre[p] = p
	else:
		cur_sum[p] = cur_sum[p-1] + a[p]
		cur_pre[p] = cur_pre[p-1]
	if cur_sum[p] > cur_max:
		cur_max = cur_sum[p]
		cur_idx = p

	p += 1

#if cur_max < 0:
#	cur_max = -9999
#	p, cur_idx = 0,0
#	while p<N:
#		if a[p] > cur_max:
#			cur_max = a[p]
#			cur_idx = p
#		p += 1

if cur_max < 0:
	cur_max = max(a)
	cur_idx = a.index(cur_max)

printArray(cur_sum)
printArray(cur_pre)
print("largest sum is", cur_max)
print("between index", cur_pre[cur_idx], cur_idx)
