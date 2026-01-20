def most_frequent(nums):
    count = {}
    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    max_num = None
    max_count = 0

    for number in count:
        if count[number] > max_count:
            max_count = count[number]
            max_num = number
    return max_num

print(most_frequent([1,2,2,3]))