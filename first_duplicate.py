def first_duplicate(nums):
    seen = set()
    for number in nums:
        if number in seen:
            return number
        else:
            seen.add(number)
    return -1
print(first_duplicate([2,1,3,5,]))
