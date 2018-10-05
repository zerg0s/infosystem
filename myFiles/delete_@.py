def dl_dd(str1):
	s1 = list(str1)
	i = 0
	while(i<len(s1)):
		if (s1[i] == '@'):
			s1[i] = ''
		i+=1
	dl = ''.join(s1)
	print(dl)
