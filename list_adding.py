list_1 = "-"
list_2 = []

while list_1 != "0":
    if list_1 in "123456":
        print("Adding {} to list".format(list_1))
        if list_1 == "1":
            list_2.append("Computer")
        elif list_1 == "2":
            list_2.append("Monitor")
        elif list_1 == "3":
            list_2.append("Keyboard")
        elif list_1 == "4":
            list_2.append("Mouse")
        elif list_1 == "5":
            list_2.append("Mouse Mat")
        elif list_1 == "6":
            list_2.append("Hdmi Cable")
    else:
        print("Please add options from the list below.")
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: Mouse")
        print("5: Mouse Mat")
        print("6: Hdmi Cable")
        print("0: Finished")
    list_1 = input()
print(list_2)
