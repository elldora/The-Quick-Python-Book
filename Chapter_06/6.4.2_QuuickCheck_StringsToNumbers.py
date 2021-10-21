'''
QUICK CHECK: STRINGS TO NUMBERS
Which of the following will not be converted to numbers, and why?

a = int('a1')
b = int('12G', 16)
c = float("12345678901234567890")
d = int("12*2") 
'''

a = int('a1', 10) # invalid literal for int() with base 10: 'a1'
b = int('12F', 16) # invalid literal for int() with base 16: '12G'
c = float("12345678901234567890") # this is convertable
d = int("12*2") # invalid literal for int() with base 10: '12*2'

print(a)
print(b)
print(c)
print(d)
