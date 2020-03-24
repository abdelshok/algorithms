### Easy: Unique Number of Occurences
### Problem: Given an array of integers arr, write a function that returns true 
### if and only if the number of occurences of each value in the array is unique
###

### Beats 97% of time complexity submissions and 100% of space complexity
### O(N) time complexity, O(N) space complexity

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashTable = self.getHashOccurences(arr)
                
        arrOccurrences = []
        
        for key in hashTable.keys():
            occur = hashTable[key]
            arrOccurrences.append(occur)
            
        setOccurrences = set(arrOccurrences)
        
        return False if len(setOccurrences) != len(arrOccurrences) else True
    

    def getHashOccurences(self, arr):
        hashTable = {}
        for num in arr:
            if num in hashTable:
                hashTable[num] += 1
            else:
                hashTable[num] = 1
                
        return hashTable