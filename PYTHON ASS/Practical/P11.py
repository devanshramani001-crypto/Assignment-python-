# Write a Python function to get the largest number, smallest num and sum of all from a list.

def list_stats(numbers):
 
    largest = max(numbers)
    
    smallest = min(numbers)
    
    total = sum(numbers)

    return largest, smallest, total

my_list = [10, 20, 5, 40, 15]

largest_num, smallest_num, total_sum = list_stats(my_list)

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", total_sum)