### Easy
### Badly explained on Leetcode: Given a non-empty array of digits representing a non-negative integer, incrmenet that integer
### ie. [1,2,4] --> 124 --> 125 --> [1,2,5]
### Link: https://leetcode.com/problems/plus-one/

### Solution implemented: O(N) time, O(1) space (constant)
### Beats 70% - few other solutions. Could be due to the fact that the easiest solution involves joining the array, transofrming it into
### a string, then a number, adding + 1, transforming it back into a string, and then bak into a list?
### Arguable though since that involves so many for loops (O(N) * x, which still ends up being O(N))

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 0
        
        for i in range(length-1, -1, -1):
            if i == length-1: # If it's the first element
                carry = 0 if digits[i] + 1 < 10 else 1
                digits[i] = (digits[i] + 1) if digits[i] + 1 < 10 else 0
            elif i >= 0 and i < length-1:
                # If we're at the back then no special rules apply yet. 
                # We keep adding to the current, get the carry and move
                # to next step

                nextCarry = 0 if digits[i] + carry < 10 else 1   
                digits[i] = digits[i] + carry if digits[i] + carry < 10 else 0 
                carry = nextCarry
        
        if carry == 1: # Then we carried one number
            array = [carry] + digits
            return array
        else:
            return digits

### Second Implementation - which I consider to be cheating the initial purpose of the problem

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        num = 0
        for i in range(length):
            currDigit = digits[i]
            num += currDigit*pow(10, length-1-i)
        
        num += 1
        newDigits = list(map(int, str(num)))
        return newDigits
            