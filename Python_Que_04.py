# Finding multiples of 'X' in 'n' numbers
#i.e we will be asked for a input of number of whose multiples we want.
# (what are multiple? - when number is multiplied my natural numbers the numbers we get are multiples
#  ex. multiples of 2- 2,4,6,8,10,12,14,18,etc)
# we will aslo be asked for the border value of multiples i.e till which natural number we want 
# multiples of previously entered number

#Input
#X = 3
#N = 20

#Output
#3,6,9,12,15,18.

x = int(input("Enter a number, of whose mutliples you want. X = "))
n = int(input("Till what number do you want multiples? N = "))

print("Multiples of ", x, "till ", n, "are :- ")

for i in range(x, n+1, x):
    print(i)
