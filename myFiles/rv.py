a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

x = 0
 
if (a == 0 and b == 0):
  x = "INF"
else: 
  if (a == 0):
    x = "NO"
  else:
     x = - (b / a)
     if (c != 0):
         if (abs(x + b / c) < 0.00001):
          x = "NO"

print(x)