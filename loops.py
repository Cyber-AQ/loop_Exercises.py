# examining for loop and other loops.
# the use of continue and Break commands are seen here.
import random
names_List = ["louis", "Brice", "Alice", "Pierce", "Carlos"]

for names in names_List:
    print(names)

print()
print()
one_Name = input("enter one child of Mr& Mr's Massawe you love most here...")
found = None
for names in range(len(names_List)):
    if one_Name == names_List[names]:
        found = names
        break
print("The name is at index {}".format(found))
print()

# or we can write this way.
# for one_Name in names_List:
#     found = names_List.index(one_Name)
# print("The name is at index {}".format(found))

