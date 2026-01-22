def subarray_sum(nums,k):
    total = 0
    count = 0
    freq = {0:1}

    for num in nums:
        total += num

    if total - k in freq:
        count += freq[total-k]

    freq[total] = freq.get(total, 0) + 1


print(subarray_sum([1,1,1],2))