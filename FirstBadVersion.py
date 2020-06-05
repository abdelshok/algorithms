### First Bad Version
### Suppose you have n verisons of a software and you want to find out the first bad one.
### Create an algorithm that will find it by minimizing the number of calls to the API
### Link: https://leetcode.com/problems/first-bad-version/solution/

### Linear search obviously out of the question. Implementation of famous Binary Search with subtle
### trap.

### O(logN) time complexity, O(1) space complexity

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 0, n-1
        
        while i <= j:
            mid = j + (i-j) / 2
            
            if isBadVersion(mid):
                j = mid-1
            else:
                i = mid + 1
    
        return i