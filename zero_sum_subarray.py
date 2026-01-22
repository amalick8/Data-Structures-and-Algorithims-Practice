def zero_sum_subarray(nums):
    total = 0
    seen = set()

    for num in nums:
        total += num
    
        if total == 0:
            return True
    
        if total in seen:
            return True
    
        seen.add(total)

    return False