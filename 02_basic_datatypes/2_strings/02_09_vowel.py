'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
# Get phrase
phrase = input("Enter a phrase: ")
# Make lowercase so count isn't case-sensitive
phrase = phrase.lower()
# Count vowels
a = phrase.count('a')
e = phrase.count('e')
i = phrase.count('i')
o = phrase.count('o')
u = phrase.count('u')
y = phrase.count('y')
# Print number of vowels
print("There are", a + e + i + o + u + y, "vowel(s) in your phrase.")
# Print a count for each vowel
print("Your phrase contains", a, "'a'(s).")
print("Your phrase contains", e, "'e'(s).")
print("Your phrase contains", i, "'i'(s).")
print("Your phrase contains", o, "'o'(s).")
print("Your phrase contains", u, "'u'(s).")
print("Your phrase contains", y, "'y'(s).")
