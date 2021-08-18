'''TRY THIS: LIST OPERATIONS 

If you have a list x, write the code to safely remove
an item if—and only if—that value is in the list.
Modify that code to remove the element only if the item occurs in the list
more than once.'''

# the code to safely remove an item if—and only if—that value is in the list

x = [1, 2, 3, 3, 3, 4, 5, 6, 7]

if 2 in x:
    x.remove(2)
print(x)

# code to remove the element only if the item occurs in the list more than once.

if x.count(3) > 1:
    x.remove(3)
print(x)