'''QUICK CHECK: 
LIST OPERATIONS What would be the result of len([[1,2]] * 3)? '''

x = [[1,2]]*3
x_len = len(x)
print("x: ", x)
print("x_len: ", x_len) 
# len: 3 ---> [[1,2], [1,2], [1,2]]

'''What are two differences between using the "in" operator and a "list’s index()"
method?'''

# Differences between "in" operator and a "list’s index()" method:
 ## in operator:
 ### 1) returns True or False if the the element exists in the desiered collection
 ### 2) could be used of numerical or non-numerical elements existance

 ## "list’s index()" method:
 ### 1) it returns the index of the desiered element in the collection
 ### 2) it returns a number as a result

'''Which of the following will raise an exception?: min(["a", "b”, "c"]);
max([1, 2, "three"]); [1, 2, 3].count("one")'''

x_min = min(["a", "b", "c"])
print(x_min)

# x_max = max([1, 2, "three"]) 
# print(x_max)
# Exception has occurred: TypeError
## '>' not supported between instances of 'str' and 'int' 

x_count = [1, 2, 3].count("one")
print(x_count)


