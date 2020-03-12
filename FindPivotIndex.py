### Easy
### Problem: Find pivot index so that the sum of all the values on left side of it are equal to the sum of the values
### on the right
### https://leetcode.com/problems/find-pivot-index/

### Beats 95% of submissions
### O(N) time complexity, O(1) space complexity

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Calculate full total 
        # Have a sliding scale with total 
        # Right total = full total
        # At every iteration
        # Decrement the right total by the current element
        # Increment the left element with the left element if there is one
        # Keep doing it for the whole array
        
        rightTotal= sum(nums)
        leftTotal = 0
        length = len(nums)
        
        for i in range(length):
            currValue = nums[i]
            rightTotal -= currValue # Decrement the right total by the current value
            
            # Increment the left total by the previous value if we're not at first
            # element
            leftTotal = leftTotal + nums[i-1] if (i != 0) else leftTotal
                
            if leftTotal == rightTotal:
                return i
            
        return -1 
                