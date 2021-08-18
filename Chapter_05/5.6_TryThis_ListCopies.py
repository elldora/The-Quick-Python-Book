'''TRY THIS: LIST COPIES Suppose that you have the following list: x = [[1, 2,
3], [4, 5, 6], [7, 8, 9]] What code could you use to get a copy y of
that list in which you could change the elements without the side effect of
changing the contents of x? '''

x = [[1, 2,3], [4, 5, 6], [7, 8, 9]]
import copy
y = copy.deepcopy(x)

y[0][0]='one' 
print("x: ", x)
print("y: ", y)