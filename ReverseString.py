### Easy
### Problem: Reverse string in O(1) space
### https://leetcode.com/problems/reverse-string/submissions/

### Beats 96% submissions
### O(N) time complexity (TC), O(1) space complexity (SC)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        
        while i < j:
            leftSideChar = s[i]
            rightSideChar = s[j]
            s[j] = leftSideChar
            s[i] = rightSideChar
            
            i += 1
            j -= 1
            
        return s