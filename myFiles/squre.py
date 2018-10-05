def isPointArea(CoordinateX, CoordinateY):
 return (abs(CoordinateX) + abs(CoordinateY) <= 1)



CoordinateX = float(input('Input x\n'))
CoordinateY = float(input('Input y\n'))

if isPointArea(CoordinateX, CoordinateY) == True:
 print('YES')
else:
 print('NO')
