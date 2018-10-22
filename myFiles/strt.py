def perevor(str1):
	start = s.find('h')
	end = s.rfind('h')
	newstr = str1[0:start] + str1[end+1:start-1:-1] + str1[end:len(str1)]
	print(newstr)
