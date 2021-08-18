'''TRY THIS: MODIFYING LISTS 
Suppose that you have a list 10 items long. How
might you move the last three items from the end of the list to the beginning,
keeping them in the same order? 
'''


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[:0] = x[-3:]
del x[-3:]

print(x)