'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
# Get name
name = input("Enter your name: ")
# Print pig latin name
print("Your pig latin name is", name[1:] + name[0].lower() + 'ay')
