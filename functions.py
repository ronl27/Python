# Odd/Even:

# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

# def odd_even():
#     for count in range (1,2000):
#         if count % 2 == 0:
#             print "number is", count, "this is an even number"
#
#         if count % 2 == 1:
#             print "number is", count, "is an odd number"
#
# odd_even()

# Multiply
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

# def multiply():
#     a = [2, 4, 10, 16]
#     b = []
#     for item in a:
#         b.append(item * 5)
#     print b
#
# multiply()

# Hacker Challenge
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list.

# def layered_multiplies(arr):
#     x = [2, 4, 10, 16]
#     for i in range (len(x)):
#         b = x[i] * [1]
#         print b
#
# layered_multiplies()
