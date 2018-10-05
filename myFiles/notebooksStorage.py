#Done by Danilova Irina
#When 18.09.2018
#Task: Storage of notebooks

storageLength = int(input("Enter storage length: "))
storageHeight = int(input("Enter storage height: "))
storageWidth = int(input("Enter storage width: "))
notebookBoxLength = int(input("Enter notebook length: "))
notebookBoxHeight = int(input("Enter notebook height: "))
notebookBoxWidth = int(input("Enter notebook width: "))


storageCapacity = storageHeight * storageLength * storageWidth
notebookBoxCapacity = notebookBoxHeight * notebookBoxLength * notebookBoxWidth

maxValueOfNotebooks = int(storageCapacity / notebookBoxCapacity)

print("Maximum amount of notebooks that can be placed is: ", maxValueOfNotebooks)