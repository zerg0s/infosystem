def add_zv(str1):
	s1 = list(str1)
	i = 0
	t = []
	while(i<len(s1)):
		t.append(s1[i])
		t.append('*')
		i+=1
	t[len(t)-1] = ''	
	zv = ''.join(t)
	print(zv)
