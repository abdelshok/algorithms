### Medium: Minimum Number of Steps to Make Two Strings Anagram
### Problem: Given two equa-size strings s and t. In one step you can choose any character
### of t and replace with another character. Return the min number of step sto mak et an 
### anagram of s
### https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


### Beats 100% submission for space complexity, 80% time complexity
### O(N) time, O(N) space

### Remember, two cases where to increase.
### First case, the number is simply not present. The second case, the number is present but
### not in that quantity (so it's value in hash) is 0 because it's being decremented, we count that.

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        hashTable = {}
        lengthS = len(s)
        lengthT = len(t)
        
        counter = 0

        for char in s:
            if char in hashTable:
                hashTable[char] += 1
            else:
                hashTable[char] = 1

        for char in t:
            if char in hashTable and hashTable[char] > 0:
                hashTable[char] -= 1
            else:
                counter += 1

        return counter
            
            