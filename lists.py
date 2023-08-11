print([1,2,3,4,5])

#difference between list and array
#1.array is homogenous, list is heterogenous
#2. list does not store elements in contiguous memory
#3. arrays are faster
#4. list are programmer friendly

#types of lists in python
#empty list
L=[]
print(L)

#homogenous list
L=[1,2,3,4,5]
print(L)

#heterogenous list
L=[1,2,3,"Apple",1.9,True]
print(L)

#multidimensional list
#2d list homogenous
L=[[1,2,3],[4,5,6],[7,8,9]]
print(L)

#2d list heterogenous
L=[1,2,[4,5]]
print(L)

#3d list
L=[[[4],[9,0]],[[1,7],[6,9,8]]]
print(L)

#string to list/list function
L=list('Vanshika')
print(L)

#indexing in list
#prints first character,here V
print(L[0])
#negative indexing prints characters from last,here a
print(L[-1])
print(L[-2])

#print in range 3 is not inclusive
print(L[1:3])

#reverse the list in range 1:3
print(L[3:1:-1])

#reverse complete list
print(L[::-1])

L=[[[4],[9,0]],[[1,7],[6,9,8]]]
print(L[0][1][1]) #output will be zero

#update items in list
#lists in python are mutable
L=[1,2,3,4,5]
L[3]=9
print(L)

L[2:4]=[19,40]
print(L)

#add new items in list
#append, extend,insert
L.append(6)
print(L)

#it appends as complete list
L.append([1,3])
print(L)

# it appends as items of the list
L.extend([2,3,40])
print(L)

L.extend('goa')
print(L)

L.append('goa')
print(L)

L.insert(1,100)
print(L)

#delete
#del
#remove
#pop
#clear

# L1=[1,2,3,4,5]
# del L1
# #error because L1 is deleted
# print(L1)

del L[0]
print(L)

del L[1:4]
print(L)

del L[-4:]
print(L)

L.insert(0,'hello')
print(L)
#remove deletes the element by value
L.remove('hello')
print(L)

#pop: removes the last element from the list
L.pop()
print(L)

#clear: clears the list but does not remove it from memory like delete
L.clear()
print(L)

