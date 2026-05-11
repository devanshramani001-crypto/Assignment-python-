# Write a Python program to get a string made of the first 2 and the last 2.

text = input("Enter a string: ")

if len(text) < 2:
    print("Empty String")
else:
  
    result = text[:2] + text[-2:]
    
    print("New string:", result)