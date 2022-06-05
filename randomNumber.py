import random

top = 10
quitting = int(input("Do you wanna quit? then type 0 or 1 for not quiting"))

while quitting == 1:  # condition is:   1 <= random_number <= top
    random_number = random.randint(1, top)
    print(random_number)
    print("Now let's see our tries!")
    number = input("enter a value in a range of 1 - 10")
    if number <= random_number:
        print("LOL! it was less than generated number that is: {0}".format(random_number))
        # random_number = random.randint(1, top)
        value = int(input("enter value above {0}".format(random_number)))
        print(random_number)
        if number == random_number:
            print("You got it right, Hurray!")
        else:
            print("you missed again!")
    elif number == random_number:
        print("You got it right at first, Hurray!")
    elif quitting == 0:
        print("Shush, atlast you are out of the boring moments")
        break
    else:
        print("The number is too higher than generated on that is: {0}".format(random_number))
        # random_number = random.randint(1, top)
        value1 = int(input("enter value less than {0}".format(random_number)))
        print(random_number)
        if number == random_number:
            print("You got it right, Hurray!")
        else:
            print("you missed again!")
    quitting = int(input("Do you wanna quit? then type 0 or 1 for not quiting"))
