#Exercise 1
list = ['ph', 'ch', 1997, 2000, 2000, 2009]  
list[2] = 2001
list.remove(2000)
list.append(2015)
print(list[2:])


# Matrix definition
data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#Access center value (row 2, col 2)
print("Center value:", data[1][1])
#Update row 2, col 2 to 25
data[1][1] = 25
print("Updated matrix:", data)
#Append 2 to second row
data[1].append(2)
print("After appending 2:", data)


L = ['a', 'b', 'c']
#Normal indexing
print("L[2]:", L[2])
#Negative indexing
print("L[-2]:", L[-2])
#Slicing
print("L[1:]:", L[1:])
