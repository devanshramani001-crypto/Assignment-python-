# Write a Python function to reverses a string if its length is a multiple of 4.

def reverse_if_multiple_of_four(text):
    if len(text) % 4 == 0:
        return text[::-1]  
    return text             

string = input("Enter a string: ")
print("Result:", reverse_if_multiple_of_four(string))