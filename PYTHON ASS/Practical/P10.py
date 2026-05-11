# Write a Python function to insert a string in the middle of a string. 

def insert_in_middle(original, to_insert):

    middle = len(original) // 2
    
    new_string = original[:middle] + to_insert + original[middle:]
    
    return new_string

main_string = input("Enter the main string: ")
insert_string = input("Enter the string to insert: ")

result = insert_in_middle(main_string, insert_string)

print("New string after insertion:", result)