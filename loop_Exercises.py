# question 1. Print First 10 natural numbers using while loop
# i = 0
# while i <= 10:
#     print("for i is equal to {}".format(i))
#     i += 1

# question 2. Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print('')
#
# for i in range(rows):
#     print(i)
#     # nested loop
#     for j in range(i):
#         print(j)
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print('')

# simple.for.2.py
# surnames = ['Rivest', 'Shamir', 'Adleman']
# for position in range(len(surnames)):
#     print(surnames[position], end='')
# print()

# question 3. Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
# summation = 0
# user3 = int(input("Enter a number!"))
# initial = 1
# print("your value is {}".format(user3))
# while initial <= user3:
#     summation = summation + initial
#     initial += 1
# print("The sum of {} is {}".format(user3, summation))


# question 4. Write a program to print multiplication table of a given number
# user4 = int(input("Enter a number!"))
# print("MULTIPLICATION TABLE OF {}".format(user4))
# print("-" * 12)
# for w in range(user4 + 1):
#     print("{} x {} = {}".format(user4, w, user4 * w))
# print("-" * 12)

# question 5. Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# index = 0
# while index < len(numbers):
#     if numbers[index] % 5 == 0 and not(numbers[index] > 150) and (numbers[index] != 500):
#         print(numbers[index])
#     elif numbers[index] > 150:
#         continue
#     elif numbers[index] > 500:
#         pass
#         break
#     index += 1


# numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # check if number is divisible by 5
#     elif item % 5 == 0:
#         print(item)

# question 6.Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
#
# For example, the number is 75869, so the output should be 5.


# question 7. Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# for i in range(1, 6):
#     for j in range(i, 6):
#         print(j, end="")
#     print()

# question 8. Print list in reverse order using a loop
# number = 10987654321
# for n in number:
#     print(n.)

# question 9. Display numbers from -10 to -1 using for loop
# for i in range():
#     print()

# question 10. Use else block to display a message “Done” after successful execution of for loop

# question 11. Write a program to display all prime numbers within a range
# A Prime Number is a number that cannot be made by multiplying other whole numbers.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.
# for i in range(25, 51):
#     if i > 1:
#         for notPrime in range(2, i):
#             if (i % notPrime) == 0:
#                 break
#         else:
#             print(i)

# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)

# question 12. Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers.
# The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

# question 13. Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
#
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
#
# For example: calculate the factorial of 5

# question 14. Reverse a given integer number

# question 15. Use a loop to display elements from a given list present at odd index positions

# question 16. Calculate the cube of all numbers from 1 to a given number
# Write a program to print the cube of all numbers from 1 to a given number
#
# Given:
# input_number = 6

# question 17. Find the sum of the series up-to n terms
# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# question 18. Print the following pattern
# Write a program to print the following start pattern using the for loop
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
