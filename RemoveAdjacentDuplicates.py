### Remove Adjacent Duplicates
### Easy: As the title suggests
### https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

### O(N) time complexity, O(1) space complexity
### Use stack

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Use stack to remove all the adjacent charaters
        stack = []
        string = S
        counter = 0
        
        for char in string:
            
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char )
        
        return ''.join(stack)