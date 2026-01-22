def most_frequent(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    max_num = None
    max_count = 0

    for num in count:
        if count[num] > max_count:   
            max_count = count[num]
            max_num = num

    return max_num 

print(most_frequent([1,2,2,2,2,4]))


    