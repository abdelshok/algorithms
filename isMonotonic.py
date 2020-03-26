### Easy: Is Monotonic?
### Problem: Is array monotonic ascending or descending?
### https://leetcode.com/problems/monotonic-array/

### Honestly, to anyone reading this, I'm going to be real with you. Beats 100% space complexity submissions, but both algorithms 
### only beat 60% of submissions for time complexity. I should be ashamed and I am. It is 100% a competition. 
### O(N) time complexity, O(1) space (constant) complexity 

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # More elegant solution is to do a one-pass with two variables.
        # Much cleaner.
        
        monotonicAsc = monotonicDesc = True
        length = len(A)
        
        for i in range(length-1):
            currEl = A[i]
            nextEl = A[i+1]
            if currEl < nextEl:
                monotonicDesc = False
            if currEl > nextEl:
                monotonicAsc = False
            
        return monotonicAsc or monotonicDesc


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Brute force is to simply check the relation between every single element
        # and it's adjacent one (i+1)
        # Both for the increasing monotonic or decreasing monotonic
        # Set a boolean
        # After every single loop, check if the booelan is positive and return it if
        # it is
        # Reset the boolean to be True right after and do the opposite loop. 
        
        length = len(A)
        monotonic = True
        
        for i in range(length-1):
            currEl = A[i]
            nextEl = A[i+1]
            if currEl > nextEl:
                monotonic = False
            
            # If it's increasingly monotonic, then this if statement will never be hit
            # and monotonic will never change to False
        
        if monotonic == True:
            return monotonic
    
        # Now if we get here, we've ascertained that the array is not increasingly 
        # monotonic
        # We therefore check if the array is decreasingly monotonic
        monotonic = True
        
        for i in range(length-1):
            currEl = A[i]
            nextEl = A[i+1]
            if currEl < nextEl:
                monotonic = False
        
        return monotonic