### Easy
### Problem: Reverse vowels in a string. Very downvoted on LeetCode for some reason
### https://leetcode.com/problems/reverse-vowels-of-a-string/

### Beats 90% of space complexity
### Advice: 1. Don't forget to take in account capital letters. When it comes to strings,
### think about the range included (latin char only? capital vs. not? punctuation? etc.)
### 2. No need to re-invent the wheel, use list(string) in order to transform the string into
### an array
### 3. Clarity over cleverness. Always.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two pointers
        # Stop when they found a vowel
        # When they found one, they interchange them
        # Keep doing that until they meet each other or one surpasses the other 
        
        
        length = len(s)
        s = list(s)
        i, j = 0, length-1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        while i < j:
            rightChar = s[j]
            leftChar = s[i]

            if rightChar not in vowels:
                j -= 1
            elif leftChar not in vowels:
                i += 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        newString = "".join(s)
        return newString
