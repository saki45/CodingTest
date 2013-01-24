with open('test.txt') as fin:
	with open('output.txt', mode = "w") as fout:
		a = []
		for line in fin:
			a.append(line)
		a.sort()
		if(len(a) == 1):
			fout.write(a[0])
		else:
		# i is the cursor for the current position
		# j is the cursor to detect whether the j-th element is the same as i-th
			i, j, count = 0,1,0
			while j < len(a):
				count += 1
				fout.write(a[i])
				while j < len(a) and a[j] == a[i]:
					j += 1
				i = j
		print(len(a), count, sep = ":")
