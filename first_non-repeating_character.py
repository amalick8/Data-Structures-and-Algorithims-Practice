# 🚀 Problem: First Non-Repeating Character
# 
# Given a string, return the first character that does NOT repeat.
# If all characters repeat, return "None".
#
# Example 1:
# Input: "google"
# Output: "l"
#
# Example 2:
# Input: "aabb"
# Output: "None"
#
# Steps hint (if you get stuck):
# 1. Loop through the string and count how many times each character appears.
# 2. Loop through the string again and find the first character with count == 1.
# 3. If no such character, return "None".
#
# ✍️ Your job: write the function first_non_repeating(s: str) that solves this.


word = input('Enter the word you want to check for which character does not repeat: ')

def freqLetters():

    counts = {}

    for letter in word.lower():
        if letter in counts:
            counts[letter] += 1
        else:
             counts[letter] = 1
    
    for letter in word.lower():
        if counts[letter] == 1:
            return letter

    return 'None'    

print(freqLetters())





      

