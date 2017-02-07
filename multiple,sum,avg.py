# Multiples:
#
#     Part I
#         Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use an array to do this exercise.
#     Part II
#         Create another program that prints all the multiples of 5 from 5 to 1,000,000.
#
# Sum List
#
#     Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
#
# Average List
#
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]


#Part I,  code will run to print 1 - 1000, providing only odd numbers.
# for count in range(0, 1000):
#     if count % 2 == 1:
#         print count

#Part II, code will run to print 5 to 1,000,000 in multiples of 5.
# for count in range (1, 200001):
#     count = count * 5
#     print count

#code will print the sum of all the values in the given list:

# a = [1, 2, 5, 10, 255, 3]
# sum = 0
#
# for i in range( len(a)):
#     sum += a[i]
#     print sum

#Code will provide the average of the given list:

# a = [1, 2, 5, 10, 255, 3]
# count = 0
# total = 0
# avg = 0
#
# for i in a:
#     total += i
#     count += 1
#     avg = total/count
#     print "Average:", avg
