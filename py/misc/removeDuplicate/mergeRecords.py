import shutil
shutil.copyfile('output.txt', 'outputTmp.txt')

with open('test.txt') as fin:
	with open('outputTmp.txt', mode = 'r') as fin2:
		with open('output.txt', mode = 'w') as fout:
			ain, ain2, cin = [], [], []
			# read in records from the local and new record
			for line in fin:
				ain.append(line)
			for line in fin2:
				ain2.append(line)

			ain.sort()
			# remove duplicate records in the new file
			if(len(ain) > 1):
				i, j = 0, 1
				while j < len(ain):
					cin.append(ain[i])
					while j < len(ain) and ain[i] == ain[j]:
						j += 1
					i = j
					j += 1
			# merge two sorted records	
			i, j, count = 0, 0, 0
			while i < len(ain2) and j < len(cin):
				if(ain2[i] < cin[j]):
					fout.write(ain2[i])
					i, count = i+1, count+1
				elif(ain2[i] > cin[j]):
					fout.write(cin[j])
					j, count = j+1, count+1
				else:
					fout.write(cin[j])
					i, j, count = i+1, j+1, count+1
			# merge the rest records
			while i < len(ain2):
				fout.write(ain2[i])
				i, count = i+1, count+1
			while j < len(cin):
				fout.write(cin[j])
				j, count = j+1, count+1
			print(len(ain2)+len(cin), count, sep=':')

import os
os.remove('outputTmp.txt')
