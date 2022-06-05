print('Hello World')
copyPaste = input('copy the word above and paste it here!')
print(copyPaste)

# now we shall deal with strings on single and double quotations.

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".') #put forward slash for a quotation in a sentence.
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("""The pet shop owner said "No, no, 
'e's uh,...he's resting". """)
# or for printing lines within a new line!
anotherString = """This string has been 
split over 
several
lines"""

print(anotherString)

# let's now print the forward slash(\)
# print("C:\User\tonight\notes.txt")  # error for interprating \n and \t.
print(r"C:\User\Tonight\notes.txt")# use raw to print the \ without an error interpretation.
print("C:\\User\\Tonight\\notes.txt")# use the double forward slash \\ for removing error.