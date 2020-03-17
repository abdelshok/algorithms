### Easy
### Problem: Given a string with input '(', '[', '{', etc. determine if string is valid
### https://leetcode.com/problems/valid-parentheses/submissions/

### Beats 99% of submissions for time complexity
### O(N) time complexity, O(N) space complexity

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Two rules
        # Erroneous if we have the stack of each parenthesis filled at the end
        # Erroneous if we try to add a closing parentheses of any kind in a stack
        # that is currently empty
        # These two rules break the code. If by the time, we're out of the loop, 
        # all of our stacks are empty, then, we can return True :)
        
        stack = []
        stackLength = 0
        length = len(s)
        
        for index in range(length):
            char = s[index]
            
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                stackLength += 1
            else:
                if stackLength == 0:
                    return False
                else:
                    if char == ')': 
                        if stack[-1] == '(':
                            stack.pop()
                            stackLength -= 1
                        else:
                            return False
                    elif char == ']':
                        if stack[-1] == '[':
                            stack.pop() # Remove last element
                            stackLength -= 1
                        else:
                            return False
                    elif char == '}':
                        if stack[-1] == '{':
                            stack.pop()
                            stackLength -= 1
                        else:
                            return False
                        
        if stackLength == 0:
            return True
        else:
            return False