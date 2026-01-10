# Challenge 1: Sorting

# Step 1: Get input from the user
user_input = input("Enter words separated by commas: ")

# Step 2: Split the string into a list
words = user_input.split(",")

# Step 3: Sort the list alphabetically
words.sort()

# Step 4: Join the sorted list back into a string
sorted_words = ",".join(words)

# Step 5: Print the result
print(sorted_words)


# Challenge 2: Longest Word

def longest_word(sentence):
    # Step 2: Split the sentence into words
    words = sentence.split()

    # Step 3: Initialize variables
    longest = ""

    # Step 4: Iterate through the words
    for word in words:
        # Step 5: Compare word lengths
        if len(word) > len(longest):
            longest = word

    # Step 6: Return the longest word
    return longest
