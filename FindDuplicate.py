### Medium
### Find Duplicate in Array with num from 1 to n inclusive where there is a 
### repeated number in O(1) space, without modifying the array, and also by keeping
### the time complexity below O(N^2)
### Link:

### O(N) time and O(1) space
### Beats 98% of time complexity

class Solution(object):
    def findDuplicate(self, nums):
        return (sum(nums)-sum(set(nums))) / (len(nums) - len(set(nums)))

### Naive solutions that don't fit the problem criteria
### 1. Sorting 
### 2. Using sets

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        for i in range(length-1):
            currNum = nums[i]
            nextNum = nums[i+1]
            
            if currNum == nextNum:
                return currNum
