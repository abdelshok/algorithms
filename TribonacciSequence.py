### Easy: Tribonnaci Sequence
### Problem: Same as Fibo but (n) + (n-1) + (n-2)
### 

### O(N) time complexity, O(1) space (no recursive stack, using memoization)
### Beats 97% of time submission, 100% of space submissions

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # At N-th number, you subtract the number 
        triSequence = [0,1,1]
        if n <= 2:
            return triSequence[n]
        else:
            counter = 2
            
            while counter < n:
                triSequence.append(triSequence[counter-2]+triSequence[counter-1]+triSequence[counter])
                counter += 1
            
            return triSequence[-1]