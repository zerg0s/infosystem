def del_th(str1):
	s1 = list(str1)
	i = 0
	t = []
	while(i<len(s1)):
		if(i % 3 != 0):
			t.append(s1[i])
		i+=1	
	zv = ''.join(t)
	print(zv)
