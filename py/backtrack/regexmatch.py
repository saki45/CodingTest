def regexmatch(s, p):
	# match the string s with regular expression p
	if len(s)*len(p) == 0:
		return

	print()
	print(''.join(s))
	print(''.join(p))

	for i in range(0, len(s)):
		regexmatchrecur(s, i, i, p, 0)

def regexmatchrecur(s, st, scur, p, pcur):
	if scur == len(s):
		return
	if pcur == len(p):
		print(st,scur-1, "".join(s[st:scur]))
		return

	if pcur == len(p)-1:
		if p[pcur] == '.' or p[pcur] == s[scur]:
			regexmatchrecur(s, st, scur+1, p, pcur+1)
		return

	if p[pcur+1] != '*' and p[pcur+1] != '+':
		if p[pcur] == '.' or p[pcur] == s[scur]:
			regexmatchrecur(s, st, scur+1, p, pcur+1)
	else:
		if p[pcur+1] == '+':
			if p[pcur] == '.' or p[pcur] == s[scur]:
				regexmatchrecur(s, st, scur+1, p, pcur+2)
				regexmatchrecur(s, st, scur+1, p, pcur)
		else:
			if p[pcur] == '.' or p[pcur] == s[scur]:
				regexmatchrecur(s, st, scur, p, pcur+2)
				regexmatchrecur(s, st, scur+1, p, pcur+2)
				regexmatchrecur(s, st, scur+1, p, pcur)
	
if __name__ == "__main__":

	pattern1 = list("ab*bc")
	pattern2 = list("ab+bc")
	pattern3 = list("a.*bc")
	sstr = list("acabcabbcabbbcabbbbcabc")

	regexmatch(sstr, pattern1)
	regexmatch(sstr, pattern2)
	regexmatch(sstr, pattern3)
