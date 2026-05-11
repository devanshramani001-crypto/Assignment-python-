# Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a letter: ")

letter = letter.lower()

if letter in ('d', 'e', 'v', 'r', 'y'):
    print(letter, "is a vowel.")
else:
    print(letter, "is not a vowel.")