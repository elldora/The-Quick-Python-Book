'''QUICK CHECK: STRINGS TO NUMBERS
 Which of the following will not be converted to numbers, and why?
int('a1')
int('12G', 16)
float("12345678901234567890")
int("12*2") 
'''

a = int('a1', 11) # invalid literal for int() with base 10: 'a1'
b = int('12F', 16) # invalid literal for int() with base 16: '12G'
c = float("12345678901234567890") # this is convertable
d = int("122") # invalid literal for int() with base 10: '12*2'

print(a)
print(b)
print(c)
print(d)