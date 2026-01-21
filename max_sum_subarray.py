# Given a list of integers and a number k, find the maximum sum of any k consecutive elements.
# numbers = [2,1,5,1,3,2]
# k = 3
# output = 9 ✅
# 2+1+5 = 8 X
# 1+5+1 = 6 X
# 5+1+3 = 9 ✅
# 1+3+2 = 6 X

# we need to make a window of size k
# move it one step at a time
# keep current 

def max_sum_subarray(numbers, k):
    current_sum = sum(numbers[:k])
    max_count = current_sum

    for i in range(k,len(numbers)):
        current_sum = current_sum + numbers[i] - numbers[i-k]
        max_count = max(max_count,current_sum)
    
    return max_count

    


print(max_sum_subarray([4,5,2,6,1,1],3))

