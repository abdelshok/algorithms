### Easy
### Find Error Nums: Set of nums from 1 to n, one missing, one repeated, v easy
### Link: https://leetcode.com/problems/set-mismatch/submissions/


### Version1 
### O(N) time complexity, O(N) space complexity

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Put all the numbers from set S into a hash table with the key being
        # the number and the value being it's count (# of times it appears)
        # Loop through 1 to n, if count of a num is 2, store it, if a num isn't there
        # store it into array
        # Return array
        hashOfNums = transformIntoHash(nums)
        length = len(nums)
        finalArray = []
        
        for i in range(1, length+1):
            currentNum = i
            if currentNum in hashOfNums:
                value = hashOfNums[currentNum]
                # If value is two then num has been repeated
                if value == 2:
                    lengthFinal = len(finalArray)
                    # If array is empty we simply add it
                    if lengthFinal == 0:
                        finalArray.append(currentNum)
                    else:
                        finalArray = [currentNum] + finalArray
            # If number is absent
            else:
                finalArray.append(currentNum)
            
        return finalArray
    
                
def transformIntoHash(numArray):
    hashTable = {}
    for num in numArray:
        if num in hashTable:
            hashTable[num] += 1
        else:
            hashTable[num] = 1
    return hashTable

