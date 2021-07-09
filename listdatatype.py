#list is mutable data type means you can add, subtract data from it. []
a = [1,3,4,6,8,9]
#print(type(a))

# indexing starts from 0 and negative indexing start from -1
print(a[1])
print(a[-1])

# you can add data in list. for which you can use append or insert method. 

a.append(6)
print(a)

a.insert(1,10)
print(a)

#remove data from list 
a.remove(3)
print(a)

a.pop(3)
print(a)

#delete
#del a
print(a)

# for sorting data 
a.sort()
print(a)
a.sort(reverse=True)
print(a)