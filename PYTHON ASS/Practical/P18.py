# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word_length(words):
    longest = 0
    
    for word in words:
        if len(word) > longest:
            longest = len(word)
    
    return longest

word_list = ["apple", "banana", "cherry", "watermelon"]
print("Length of the longest word is:", longest_word_length(word_list))