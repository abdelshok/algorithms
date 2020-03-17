### Easy
### Problem (dynamic programming): Max contiguous subarray sum, return it.
### https://leetcode.com/problems/maximum-subarray/

### Beats 99.6% of submissions
### O(N) time complexity, O(1) space complexity

### Remember: the order in which you save the max sum. If numbers were all positive
### there would be no complexity to this problem, obviously. But the fact is, it is
### possible for all numbers to be negative, which is why it's important to save
### the maxSum (which would be the smallest negative integer in that case so arr of one)
### before resetting the counterTotal to 0

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # As long as the total number that we are looking at is above 0, then
        # we can keep it
        # If the number that we're at is below 0, then we simply reset the counter
        
        counterTotal = 0
        maxCount = float('-inf')
        
        for num in nums:
            counterTotal += num
            
            maxCount = counterTotal if counterTotal > maxCount else maxCount
            counterTotal = 0 if counterTotal < 0 else counterTotal
            
        return maxCount
        