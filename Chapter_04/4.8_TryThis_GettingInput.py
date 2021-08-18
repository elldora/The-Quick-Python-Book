''' TRY THIS: GETTING INPUT Experiment
with the input() function to get string and integer input. 
Using code similar to the previous code, what is the effect 
of not using int() around the call to input()for integer input? 
Can you modify that code to accept a float—say, 28.5? 
What happens if you deliberately enter the wrong type of value? 
Examples include a float in which an integer is expected and 
a string in which a number is expected—and vic versa'''

'''name = input("What is Your Name? ")
print("You entered { ", name , " } as your name!")'''

'''age = int(input("What is Your Age? "))
print("You entered { ", age + 1, " } as your age!")
#Result: 30 
#Result: Error: invalid literal for int() with base 10 for float input '''

'''age = input("What is Your Age? ")
print("You entered { ", age + 1, " } as your age!")
#Result: Error: invalid literal for int() with base 10 for float input '''

age = float(input("What is Your Age? "))
print("You entered { ", age + 1, " } as your age!")
#Result: 30.0