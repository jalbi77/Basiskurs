# Exercise 1: Print First 10 natural numbers using while loop

# number = 1
# while number <= 10:
#     number += 1
#     print(number)
# ************************************************************************

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# row = 5
#
# for i in range(1, row+1, 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print('')
# ************************************************************************

# Exercise 3: Calculate the sum of all numbers from 1 to a given number

# number = int(input('Nummer: '))
# s = 0
#
# for i in range(1, number + 1, 1):
#     s += i
#
# print(s)
#
# # or..
# x = sum(range(1, number + 1))
# print(x)
# ************************************************************************

# Exercise 4: Write a program to print multiplication table of a given number

# number = int(input('Number: '))
# end = int(input('End: '))
#
# for i in range(number, end+1, number):
#     print(i)
# ************************************************************************

# Exercise 5: Display numbers from a list using loop:
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)
# ************************************************************************

# Exercise 6: Count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.

# number = int(input('Number: '))
# counter = 0
#
# while number != 0:
#     number = number // 10  # 'Shift coma'
#     counter += 1
# print(counter)
# ************************************************************************

# # Exercise 8: Print list in reverse order using a loop
#
# list1 = [10, 20, 30, 40, 50]
#
# # x = reversed(list1)
# # for i in x:
# #     print(i)
#
# # or
# y = len(list1) - 1
# for i in range(y, -1, -1):
#     print(list1[i])

