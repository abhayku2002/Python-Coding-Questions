'''
Program to find factorial of a number
#i.e multiplying a entered number with all the previous natural number.

#Example:
# if 
# input = 5

# then
# 1x2x3x4x5 = 120

# output will be 120.

#Factorial is only possible of positive Numbers so input must be positive to get valid answer
'''


n = int(input("Enter the number you want factorial of :- "))
if n > 0:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("Factorial of", n, " = ", fact)
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("Enter a Valid Number")
