### Very Easy:  Max Consecutive Ones
### Problem: Given a binary array, find the max number of consecutive ones
### https://leetcode.com/problems/max-consecutive-ones/

### Beats 99% of submissions
### O(1) space complexity, O(N) time complexity

### Solution seems to be using an abstract sliding window

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Keep track of current total to have idea of consecutive 1s
        # Start at beginning
        # If num is 1, then add it
        # Move to next step
        # If num is 0, then store the curr_num in variable max if curr_total > max
        # Reset the counter to 0
        # Keep moving forward
        # Repeat
        # At the end, possibility last num is 1, which means comparison to curr_max
        # won't be made. Don't forget to do it.
        
        curr_total = 0
        curr_max = float('-inf')
        for number in nums:
            if number == 1:
                curr_total += 1
            elif number == 0:
                curr_max = curr_total if curr_total > curr_max else curr_max
                curr_total = 0 # Reset it to 0
                
        curr_max = curr_total if curr_total > curr_max else curr_max
        return curr_max