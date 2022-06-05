# 3.4 Exercises
# The following exercises should all be completed with loops.
# In some cases the exercise specifies what type of loop to use.
# In other cases you must make this decision
# yourself. Some exercises can be completed easily with both for loops and
# while loops. Other exercises are much better suited to one type of loop than the
# other. In addition, some exercises require multiple loops. When multiple loops
# are involved one loop might need to be nested inside the other. Carefully consider
# your choice of loops as you design your solution to each problem.


# Exercise 63: Average
# (26 Lines)
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
# Hint: Because the 0 marks the end of the input it should not be included in the
# average.

# print("Lets ge the average of your values. Enter one value at a time.")
# value = int(input("Enter a value, or 0 to terminate the program"))
# total = 0
# avg = 0
# a = 0  # for counting values entered by the user.
#
# while value != 0:
#     total += value
#     a += 1
#     avg = total / a
#
#     value = int(input("Enter a value, or 0 to terminate the program"))
#
# if avg == 0:
#     print("Wrong first attempt of {} value.".format(avg))
#
# print("Average is: {}".format(avg))


# Exercise 64: Discount Table
# (18 Lines)
# A particular retailer is having a 60 percent off sale on a variety of discontinued
# products. The retailer would like to help its customers determine the reduced price
# of the merchandise by having a printed discount table on the shelf that shows the
# original prices and the prices after the discount has been applied. Write a program that
# uses a loop to generate this table, showing the original price, the discount amount,
# and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
# that the discount amounts and the new prices are rounded to 2 decimal places when
# they are displayed.

price = [4.95, 9.95, 14.95, 19.95, 24.95]
calculating = (40/100)
for items in price:
    discount = calculating * price

    print("Original price: ${} | Discounted: ${}".format(items, discount))


# Exercise 65: Temperature Conversion Table
# (22 Lines)
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the Internet.