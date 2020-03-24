### Easy: Add Digits 
### Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
### https://leetcode.com/problems/add-digits/

### Beats 99% of submissions
### O(N) time complexity, O(1) space complexity (?)

### Follow up: Can you do it wihtout any loop / recursion in O(1) runtime?

### Below is the brute-force solution, which isn't elegant in any remote way.
### Elegant solution involves modulo 9 :)

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        listNum = list(str(num))
        finalNum = getTotal(listNum)
        
        while finalNum >= 10:
            listNum = list(str(finalNum))
            finalNum = getTotal(listNum)
            
        return finalNum
    
    
def getTotal(arrNumbers):
    total = 0
    for numString in arrNumbers:
        total += int(numString)
        
    return total