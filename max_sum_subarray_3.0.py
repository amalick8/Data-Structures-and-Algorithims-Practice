def max_sum_subarray(nums,k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k,len(nums)):
        current_sum = current_sum + nums[i] - nums[i-k]
        max_sum = max(current_sum, max_sum)
    return max_sum 

print(max_sum_subarray([1,2,2,2,3],3))

