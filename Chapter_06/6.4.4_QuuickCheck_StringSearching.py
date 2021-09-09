'''
QUICK CHECK: STRING SEARCHING
 If you wanted to check whether a line ends
with the string "rejected", what string method would you use? Would there
be any other ways to get the same result?
'''

x = "This request is rejected"
print(x.endswith("rejected"))

y=len("rejected")
print(x[-y:] == "rejected")

# import re   

# EndsWith = lambda x,y: re.findall('[^a-zA-Z0-9 \n\.]',y) != []
# y = "rejected"
# print(EndsWith(x, y))