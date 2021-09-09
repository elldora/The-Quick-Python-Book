'''
QUICK CHECK: FORMATTING STRINGS WITH %
 What would be in the variable x
after the following snippets of code have executed?
'''

# x1 = "%.2f" % 1.1111
# print(x1) # 1.11
# x2 = "%(a).2f" % {'a':1.1111}
# print(x2) # 1.11
x3 = "%(a).08f" % {'a':1.1111}
print(x3) # 1.11110000