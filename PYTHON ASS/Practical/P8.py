# Write a Python program to remove duplicates from a list

def remove_duplicates(my_list):

    unique_list = list(set(my_list))
    return unique_list

numbers = [10, 20, 30, 20, 40, 10, 50]

result = remove_duplicates(numbers)

print("Original List:", numbers)
print("List after removing duplicates:", result)