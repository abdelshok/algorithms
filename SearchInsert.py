


class Solution(object):
    def searchInsert(self, nums, target):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
    

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        
        while (j-i) > 1:
            middleIndex = (j+i)/2
            middleNum = nums[middleIndex]
            if middleNum == target:
                return middleIndex
            else:
                if middleNum < target:
                    i = middleIndex
                elif middleNum > target:
                    j = middleIndex
        
        leftNum = nums[i]
        rightNum = nums[j]
        
        if leftNum < target and target < rightNum:
            return i + 1
        elif target < leftNum:
            return 0
        elif target > rightNum:
            return j + 1
        elif target == leftNum and target == rightNum:
            return i # Takes care of num if there's ony [1]
        elif target == leftNum and target != rightNum:
            return i
        elif target != leftNum and target == rightNum:
            return j
            
        
    