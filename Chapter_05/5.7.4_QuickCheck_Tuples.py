'''
QUICK CHECK: TUPLES 
Explain why the following operations aren’t legal for
the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?
'''

x = (1, 2, 3, 4)

# x.append(1) # error: 'tuple' object has no attribute 'append'
# x = x+tuple(1) : 'int' object is not iterable
# # x = x+(1,) # correct


# x[1] = "hello" # error: 'tuple' object does not support item assignment; immutable

# del x[2] # error: 'tuple' object doesn't support item deletion
# Remove an Item from Tuple

numTuple = (2, 22, 33, 44, 5, 66, 77)
print("Tuple Items = ", numTuple)

numList = list(numTuple)
numList.remove(44)

numTuple1 = tuple(numList)
print("After Removing 3rd Tuple Item = ", numTuple1)

print("x: ", x)