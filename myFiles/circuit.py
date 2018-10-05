def isPointArea(NumX, NumY):
	return ((NumY - 2*NumX >= 2) and (NumX + NumY >= 0) and ((NumX + 1)**2 + (NumY - 1)**2 <= 4)) or ((NumX + NumY <= 0) and (NumY - 2*NumX <= 2) and ((NumX + 1)**2 + (NumY - 1)**2 >= 4))



a = float(input('Input x\n'))
b = float(input('Input y\n'))

if isPointArea(a, b) == True:
	print('YES')
else:
	print('NO')
