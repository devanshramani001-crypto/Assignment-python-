# Write a Python program to check a list is empty or not

def check_list(my_list):

    if len(my_list) == 0:
        print("The list is empty")
    else:
        print("The list is not empty")

list1 = []
list2 = [10, 20, 30]

check_list(list1)
check_list(list2)