#Find and Replace
#In a string like this one: str = "If monkeys like bananas, then I must be a monkey!" print the position for all instances of the word "monkey". Then create a new string where the word "monkey" is replaced with the word "alligator".

#Min and Max
#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

#First and Last
#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list.

#New list
#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort it, then slice out all of the values that are negative, placing those values in a new list. Then add your new list into the original one at position 0. The output should be: [[-3, -2], 2, 6, 7, 10, 12, 19, 32, 54, 98]. This one is tough!


# Find and replace:

# bananas = "If monkeys like bananas, then I must be a monkey!"
# print bananas.replace('monkey', 'alligator')

#Min and Max:

# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)

#First and Last:
#my_list = ["hello",2,54,-2,7,12,98,"world"]
#x = []
# print my_list[0]
# print my_list[7]
#x.append('hello')
#x.append('world')
#print x

#New List
#[[-3, -2], 2, 6, 7, 10, 12, 19, 32, 54, 98] - new array
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y= []

y.sort()
x.sort()
x.insert(0, y)
print x
x.sort()
print x
for z in x:
    if z < 0:
        print(z)
        y.insert(0,z)
# print (y)
y.sort()
# print(y)
# print(x)
x.remove(-3)
x.remove(-2)
# print(x)
x.insert(0,y)
print(x)

###################
#Sams code
# y= [i for i in x if i < 0]
# x = [i for i in x if i > 0]
# y.sort()
# x.sort()
# x.insert(0, y)
# print x
