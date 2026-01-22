def contains_duplicates(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True

print(contains_duplicates([1,2,3]))
print(contains_duplicates([2,2,3]))