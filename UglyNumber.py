### Easy: Ugly Number
### Problem: Write a program to check whether a given number is an ugly number.
### Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
### Link: https://leetcode.com/problems/ugly-number/

### Beats 92% of submissions
### O(N) time complexity

### Prime factorization problem, part of number theory.
### W/ numbers sufficiently large, no efficient, non-quantum integer factorization
### algorithm is known. Difficulty of problem (no efficient algo exists) is the heart
### of many algs in cryptography such as RSA. 

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        factors, arrOfFactors = {2,3,5}, []
        
        if num <= 0:
            return 0
        
        while num > 1: 
            if num % 2 == 0:
                arrOfFactors.append(2)
                num = num / 2
            elif num % 3 == 0:
                arrOfFactors.append(3)
                num = num / 3
            elif num % 5 == 0:
                arrOfFactors.append(5)
                num = num/5
            else:
                return False
        
        return True
    