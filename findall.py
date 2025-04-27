'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''
def findDisappearedNumbers(nums):
    result = []
    length = len(nums)
    num_set = set(nums)
    
    for element in range(1, length+1):
        if element not in num_set:
            result.append(element)
    return result


nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))