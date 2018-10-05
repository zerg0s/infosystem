def change_h(str1):
	s1 = list(str1)
	i = 0
	t = []
	j = 1
	while(i<len(s1)):
		if (s1[i] == 'h'):
			t.append(i)
		while(j<len(t) - 1):
			s1[t[j]] = 'H'
			j+=1
		i+=1
	hH = ''.join(s1)
	print(hH)
