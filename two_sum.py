# 🚀 Problem: Two Sum
#
# Given a list of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
#
# Assume:
# - There is always exactly one solution.
# - You cannot use the same element twice.
#
# Example 1:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
#
# Example 2:
# nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# 🔑 Hints:
# 1. Use two loops to check every pair (simple way).
# 2. Later, try using a dictionary for a faster solution.

nums = eval(input('Please type a list of numberes enclosed in [] and seperated with commas: '))
target = int(input('What number: '))

def twoSum(nums, target):

    targetNums = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return f'the indices are {[i,j]} but the actual numbers at those indices are {nums[i]} & {nums[j]}'
          
    return 'None of these numbers add up to the target'

print(twoSum(nums,target))