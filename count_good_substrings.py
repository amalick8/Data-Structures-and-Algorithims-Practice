# A window is just "A group of characters we are currently looking at"
# Fixed-size means: "The group is ALWAYS length k"

def count_good_substring(string,k):
    if len(string) < k:
        return 0
    
    count = 0
    window = string[0:k]
    if len(set(window)) == len(window):
        count += 1
    
    for i in range(k, len(string)):
        window = window[1:] + string[i]
        if len(set(window)) == k:
            count += 1

    return count
