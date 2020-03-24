### Medium: Design Custom Stack 
### Design custom stack with certain push, pop, and inc operations
### https://leetcode.com/problems/design-a-stack-with-increment-operation/


### O(1) time complexity for push, pop, O(K) or O(N) time complexity for inc
### Beats 80% time complexity, 100% space complexity


class CustomStack(object):
    
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
        self.counter = 0
        
    def push(self, x):
        if self.counter < self.maxSize:
            self.counter += 1 
            self.stack.append(x)
        # Do nothing if stack reached max size
    
    def pop(self):
        if self.counter == 0:
            return -1
        else:
            self.counter -= 1
            return self.stack.pop() # Returns last element added to stack
        
    def increment(self, k, val):
        length = k if k < self.counter else self.counter
        for i in range(length):
            self.stack[i] += val
