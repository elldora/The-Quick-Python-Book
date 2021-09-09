'''TRY THIS: STRING OPERATIONS Suppose that you have a list of strings in which
some (but not necessarily all) of the strings begin and end with the double
quote character:
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']'''

''''
What code would you use on each element to remove just the double quotes?
What code could you use to find the position of the last p in Mississippi?
When you’ve found that position, what code would you use to remove just
that letter? '''

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
y=[]
for i in range(len(x)):
    y.append(x[i].replace("\"",""))

print(y)

x = "Mississippi"
position = x.rfind("p")
print(position)

y = x[:position] + "" + x[position+1:]
print(y)