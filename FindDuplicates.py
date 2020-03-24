### Easy: Contains Duplicates
### Problem: Find if unsorted list contains duplicates
### https://leetcode.com/problems/contains-duplicate/

### Beats 99% of submissions
### O(N) space complexity, O(N) time complexity

### Two ways to do it:
### 1. Use hash table to keep track of already existing numbers. Simple.
### 2. Create set using set function and compare lengths. Simple.
### Other methods
### - Sorting O(NLogN)
### - Brute-force: comparing for every single number. Not good.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lenSet = len(set(nums))
        lenNum = len(nums)
        
        return True if lenSet < lenNum else False