def ssum(a,b):
	a -= 1
	b += 1
	if a != 0:
		return ssum(a,b)
	else:
		return b