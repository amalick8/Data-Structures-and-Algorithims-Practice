def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
print(containsDuplicate([1,2,2,4]))
print(containsDuplicate([1,2,3,4]))