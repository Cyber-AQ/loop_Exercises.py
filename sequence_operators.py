name = "Brice"
print(name)
# check if Brice is in name! or a sub thing!
print(name in "Brice") # true returned
print("Brice" in name) # true returned

# a way to print a value in a string concatenation using, f" words then {value name}
pi = 22/7
print(f"pi is equal to {pi}") # this is how it is supposed to be written.
# if you run this way below no results but errors.
# print("pi is equal to" + pi)  error.
print()
print(f"pi is equal to {pi:20.10f}")
print(f"pi is equal to {pi:60.10f}")


# challenge.
name = input("Input your name here...")
age = int(input("What is your age?"))
if 18 <= age <= 30:
    print("Hello, {} you are good to go on the 18-30 holiday!".format(name))
    print("we are glad you shall have fun!")
else:
    print("We are sorry for age restrictions, no holiday for you!")

# testing to print sentense marks(Quotation marks).
moneyAmount = "26,500;670:450 300,350"
marks = ""
for char in moneyAmount:
    if char.isdigit(): # you can say, if not char.isdigit()
        marks = marks + char

print(marks)
