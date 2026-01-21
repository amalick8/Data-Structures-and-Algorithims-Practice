def running_sum(nums):
    new_list = []
    recent_value = 0

    for num in nums:
        recent_value += num
        new_list.append(recent_value)
    
    return new_list
print(running_sum([1,2,3,4]))
