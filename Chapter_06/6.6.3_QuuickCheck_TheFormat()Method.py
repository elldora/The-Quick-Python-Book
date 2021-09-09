'''
QUICK CHECK: THE FORMAT() METHOD
 What will be in x when the following
snippets of code are executed?: '''

x1 = "{1:{0}}".format(3, 4) #"  4"
print(x1)

x2 = "{0:$>5}".format(3) # "$$$$3"
print(x2)

x3 = "{a:{b}}".format(a=1, b=5) # "    1"
print(x3)

x4 = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10) # "    1:$$$$3"
print(x4)
