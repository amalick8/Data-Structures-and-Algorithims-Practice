def most_common_char(word):
    count = {}

    for chars in word:
        if chars in count:
            count[chars] += 1
        else: 
            count[chars] = 1
    
    max_count = 0
    max_char = None

    for chars in count:
        if count[chars] > max_count:
            max_count = count[chars]
            max_char = chars
    return max_char

print(most_common_char('Hiiiii'))      
    