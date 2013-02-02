def perfectshuffle(a, st):
	# This function does perfect shuffle from the st-th element to the (st+3^k-1)th element

	print(st)
	print(a)

	N = (len(a)-st) // 2
	k = 1
	while st+3**k-1 < len(a):
		k += 1

	if not (st+3**k-1 == len(a)):
		ed = st+3**(k-1)-2
		thislen = (ed-st+1)//2
		swaplistsegment(a, st+thislen, st+N-1, st+N-1+thislen)
		perfectshuffle(a, st+2*thislen) 
	else:
		ed = len(a)-1
		thislen = (ed-st+1)//2

	k = 0
	seed = 3**k
	while seed < 2*thislen:
		i = (seed*2)%(2*thislen+1)
		tmpthis = a[st+i-1]
		while i!=seed:
			ni = (2*i)%(2*thislen+1)
			tmpnext = a[st+ni-1]
			a[st+ni-1] = tmpthis
			tmpthis, i = tmpnext, ni
		i = (seed*2)%(2*thislen+1)
		a[st+i-1] = tmpnext
		k += 1
		seed = 3**k
		

def swaplistsegment(a, st, mid, ed):
	# This function swaps the position of the st-th to the mid-th element. and the mid+1-th to the ed-th element

	if st < 0 or ed >= len(a):
		return

	if not st<=mid<=ed:
		return

	reverselistsegment(a, st, mid)
	reverselistsegment(a, mid+1, ed)
	reverselistsegment(a, st, ed)

def reverselistsegment(a, st, ed):
	# This function reverse the list from the st-th element to the ed-th element

	if ed >= len(a) or st < 0:
		return

	i, j = st, ed
	while i <= j:
		a[i], a[j] = a[j], a[i]
		i += 1
		j -= 1

if __name__ == '__main__':
	a = [i for i in range(1, 15)]
	import string
	b = list(string.ascii_uppercase[:14])
	c = a+b
	print(c)
	#swaplistsegment(c,0,8,17)
	#print(c)

	perfectshuffle(c, 0)
	print(c)
