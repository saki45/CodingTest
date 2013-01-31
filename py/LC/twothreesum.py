def twosum(a, s):
	i, j = 0, len(a)-1
	while i<j:
		tmp = a[i] + a[j]
		if tmp == s:
			print((a[i], a[j]), end = '')
			i += 1
		elif tmp < s:
			i += 1
		else:
			j -= 1
	print()
		
def threesum(a, s):
	i = 0
	while i<len(a)-2:
		j, k, ts = i+1, len(a)-1, s-a[i]
		if a[i]+a[j]>s:
			break
		while j<k:
			tmp = a[j] + a[k]
			if tmp == ts:
				print((a[i], a[j], a[k]),end='')
				j += 1
			elif tmp > ts:
				k -= 1
			else:
				j += 1
		i += 1
	print()

def twodiff(a, d):
	i, j = 0, 1
	while j<len(a):
		tmp = a[j]-a[i]
		if tmp == d:
			print((a[j],a[i]),end='')
			j += 1
		elif tmp > d:
			i += 1
		else:
			j += 1
	print()

def threediff(a, d):
	i = len(a)-1
	while i>1:	
		sd = a[i] - d
		j, k = 0, i-1
		while j<k:
			tmp = a[j] + a[k]
			if tmp == sd:
				print(((a[j],a[k]),a[i]), end='')
				j += 1
			elif tmp < sd:
				j += 1
			else:
				k -= 1
		i -= 1
	print()
	

if __name__ == '__main__':

	import random
	N = 20
	a = [int(random.uniform(0, 3*N)) for i in range(0, N)]
	a.sort()
	print(a)
	twosum(a, 2*N)
	threesum(a, 3*N)
	twodiff(a, N)
	threediff(a, 0)
