age = 24
name = "Brice Robert Aquiline"

print(age , name)
print(type(age),"\n",type(name))  # used to show data type in python.

a = 15
b = 3
print(a + b)
print(a - b)
print(a / b) # float division result
print(a * b)
print(a // b) # int division results different from (a / b)

# performing negatives take (total length - letter value) and we shall have same value as the letter value.
# example.
myName = "Brice Robert Aquiline"
print(myName)
print(myName[2]) # displays i
print(myName[3]) # displays c
print(myName[4]) # displays e
print()

# or we can do (21 - 2, 21 - 3, 21 - 4)
print(len(myName)) # print length of the myName string.
print(myName[2-21])
print(myName[3-21])
print(myName[4-21])
print()
print(myName[-19]) # same shit happens as above solutions.
print(myName[-18])
print(myName[-17])

# slicing use (0:9) where 0 is starting of the string length, while 9 is the ommited length of the string.
# mostly the range is from 0 - 8, 9 being excluded.
# example.
print()
print(myName[0:4]) # displays Bric.
# or
print(myName[:4]) # same result as above.
print(myName[0:5]) # displays Brice.

# we can use step slicing ( beginning: the end that is not included: steps to take)
print()
print(myName[0:5:2]) # displays Bie.

print()
print("see backward slicing")
alphabets = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabets))
print(alphabets[len(alphabets):len(alphabets)-9:-1]) # displays zyxwvuts(8 characters in reverse)
print(alphabets[len(alphabets)-10:len(alphabets)-13:-1]) # display qpo.
print(alphabets[len(alphabets)-22::-1]) # displays edcba.