"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
type(pi)
print(pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i<50:
    print(i)

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit=='orange':
    print(picked_fruit,'oranjeviy')
elif picked_fruit=='strawberry':
    print(picked_fruit,' red')
elif picked_fruit=='banana':
    print(picked_fruit, 'yallow')

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mult(n1,n2):
    a=n1*n2
    return a

# TODO: Now call the function a few times to calculate the following answers
b=mult(12,96)
print("12 x 96 =",b)
b=mult(48,17)
print("48 x 17 =",b)
b=mult(196523,87323)
print("196523 x 87323 =",b)
