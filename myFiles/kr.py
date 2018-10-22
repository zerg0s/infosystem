#Created by Petr Gusev
#kr5
#20.10.2018

skates = input().split()
children =input().split()
count = 0
newSkates = sorted(skates, reverse = True)
newChildren = sorted(children)

 
for i in newChildren:
     while newSkates and i > newSkates[-1]:
         newSkates.pop()
     try:
         newSkates.pop()
     except IndexError:
         break
     count += 1

print(count)
