### Easy: Happy Number
### Problem: Write an algorithm to determine if a number is happy (continuously sum square of it's digits until
### it equals 1)
### https://leetcode.com/problems/happy-number/

### Beats 91% of submissions, 
### O(1) time complexity, O(1) space complexity (to confirm?)
 


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Separate the numbers into array
        # Raise them to power of two
        # Sum them
        # Do that until it is equal to one

        
        n = sum(map(powerTwo, map(int, list(str(n)))))
        hashNums = {2, 3, 4, 5, 6, 7, 8, 9}
        
        while n != 1:
            n = sum(map(powerTwo, map(int, list(str(n)))))
            
            if n in hashNums:
                return False
            
        return True

def powerTwo(num):
    return num ** 2