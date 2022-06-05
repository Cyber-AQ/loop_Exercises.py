option = ["Exit", "Learn python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
print("Please choose your option from the list below:")

for i in range(len(option)):
    print("{}:  {}".format(i, option[i]))

while True:
    user_data = int(input())
    if option[user_data] == "Exit":
        print("try again!")
        break
    else:
        print("You chose {} as your answer! which is {}".format(user_data, option[user_data]))

