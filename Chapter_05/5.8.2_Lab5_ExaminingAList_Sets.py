'''
LAB 5: EXAMINING A LIST 
In this lab, the task is to read a set of temperature
data (the monthly high temperatures at Heathrow Airport for 1948 through
2016) from a file and then find some basic information: 
the highest temperatures
the lowest temperatures 
the mean (average) temperature
the median temperature (the temperature in the 
middle if all the temperatures are sorted)
'''

import os

file_name = "lab_05.txt"
dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + file_name
print(dir_path)

temperatures = []
with open(dir_path, 'r') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print("maximum temp: ", max(temperatures))
print("minimum temp: ", min(temperatures))
print("mean temp: ", round(sum(temperatures)/len(temperatures), 2))

sorted_temp = sorted(temperatures)
x = len(sorted_temp)

if(x%2==0):
    med1 = sorted_temp[(x//2)-1]
    med2 = sorted_temp[(x//2)]
    print("median = ", (med1+med2)/2)
elif(x%2!=0):
    med1 = sorted_temp[x//2]
    print("median = ",med1)