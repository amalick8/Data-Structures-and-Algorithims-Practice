# A set is better than a list for checkin vowels because:
# A set answers is this in here instantly
# A list has to check one by one

# There is nothing to slide first so we need a starting count
# Sliding only checks 2 characters, the one entering and the one leaving

# Best is needed instead of returning the last count because:
# The window can shrink later
# The maximum might happen earlier.

def max_vowels(s,k):
    left = 0
    current = 0
    best = 0
    vowels = {'a','e','i','o','u'}

    for right in range(len(s)):
        if s[right] in vowels:
            current += 1

        if right - left + 1 > k:
            if s[left] in vowels:
                current -= 1
            left += 1

        if right - left + 1 == k:
            best = max(best, current)

    return best

print(max_vowels("abciidef", 3))





