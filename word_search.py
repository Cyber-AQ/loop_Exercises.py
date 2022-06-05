print("Now lets sort out 's' letters in the below name")
word = "mississippi"
print(word)
known = 0
for i in word:  # for single letter
    if i == "s":
        known += len(i)

print(known)

# for multiple letter
print(word.count("iss"))
