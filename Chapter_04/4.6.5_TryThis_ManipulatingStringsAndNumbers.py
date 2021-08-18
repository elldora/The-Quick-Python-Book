'''TRY THIS: MANIPULATING STRINGS AND NUMBERS 
In the Python shell, create
some string and number variables (integers, floats, and complex numbers).
Experiment a bit with what happens when you do operations with them,
including across types. Can you multiply a string by an integer, for example,
or can you multiply it by a float or complex number? 

Also load the math module and try a few of the functions; then load the cmath module and do the
same. What happens if you try to use one of those functions on an integer or
float after loading the cmath module? How might you get the math module
functions back?'''

'''#Exercise 1:
str_var = 'elahe'
int_var = 4

result_var_1 = str_var*int_var
print(result_var_1)
#Rresult: elaheelaheelaheelahe'''

'''#Exercise 2:
str_var = 'elahe'
float_var = 4.5

result_var_2 = str_var*float_var
print(result_var_2)
#Rresult: Exception has occurred: TypeError: can't multiply sequence by non-int of type 'float' '''


'''#Exercise 3:
import cmath

str_var = 'elahe'
complex_var = 3 + 2j

result_var_3 = str_var * complex_var
print(result_var_3)
#Rresult: Exception has occurred: TypeError: can't multiply sequence by non-int of type 'complex' '''

#Exercise 4:
import math
import cmath

int_var_1 = -3
float_var_1 = 4.6
complex_var_1 = 6+5j

#result_var_4 = cmath.sqrt(int_var_1) # Result = 1.7320508075688772j
#result_var_5 = math.sqrt(int_var_1) # Result = math domain error ...
result_var_6 = math.sqrt(int_var_1)
print(result_var_6)



'''
import cmath

int_var_1 = 3
int_var_2 = 6

result_var_5 = int_var_1 * int_var_2
print(result_var_5)
#Rresult: Exception has occurred: TypeError: can't multiply sequence by non-int of type 'complex' '''

