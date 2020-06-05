### Find Special Integer 
### Find integer in sorted array that occurs more than 25% of times
### Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/

### Only beats 79% of submissions for time complexity :( but 100% of submission for space complexity :)
### 


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Obviously naive solution with O(N) time complexity and O(N) space complexity
        # would be to traverse the array and store the count of each element into 
        # a hash table, returning the one that hits 25% 
        # Element appears mor ethan 25% of time, means that the rest of elements appear
        # less than 25%
        # Cant' figure out which one appears more than 25% of the time without
        # Actually knowing the size of the array
        # If we had [1,1,1,4,4,4,4,6,6,6,7,7,8,8,8,8,8,8,8,8,8,9,9]
        # How would we know that when we're hitting the 4, it's not 25%+ of the array
        # without knowing the size of the array
        # Can't know the size of the array without doing one O(N) run to count the
        # number of elements
        # So it seems like the only solution is to actually keep track of the current
        # num with the max count and return it at the end
        
        maxCount = float('-inf')
        maxNumber = float('-inf')
        hashTable = {}
        
        for num in arr: 
            if num in hashTable:
                hashTable[num] += 1
            else:
                hashTable[num] = 1
                
            if hashTable[num] > maxCount:
                maxCount = hashTable[num]
                maxNumber = num
        
        return maxNumber
    
        