### Easy: Min Stack
### Design a stack that supports push, pop, top, and retrieving the min element
### in constant time
### https://leetcode.com/problems/min-stack/

### Beats 95% of submissions for time complexity, 91% of submissions for space complexity
### O(1) for push, pop, and return top and min

### Note to self: read about why ternary operators achieve faster results than simple if/else statements

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimumArr = []
        self.count = 0
        self.minCount = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Add to stack and increase count
        self.stack.append(x)
        self.count += 1

        # If min arr is empty, append and increment
        if self.minCount == 0:
            self.minimumArr.append(x)
            self.minCount += 1
        else:
            # If min arr isn't empty, append only if smaller than curr min
            currMinimum = self.minimumArr[-1]
            if x <= currMinimum:
                self.minimumArr.append(x)
                self.minCount += 1            

    def pop(self):
        """
        :rtype: None
        """
        if self.count == 0:
            return None
        else:
            topEl = self.stack.pop() # Removes and return last element
            self.count -= 1 # Make sure to decrement the current count
            currMin = self.minimumArr[-1]
            # If the element we removed is equal to curr min, we ensure
            # to remove curr minimum
            if currMin == topEl:
                self.minimumArr.pop()
                self.minCount -= 1

    def top(self):
        
        return self.stack[-1] if self.count != 0 else None

    def getMin(self):
    
        return self.minimumArr[-1] if self.minCount != 0 else None
        
