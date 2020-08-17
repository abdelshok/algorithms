### Medium: Binary Search Tree Iterator
### Implement next() and hasNext() functions in O(1) time complexity to find next smallest integer
### https://leetcode.com/problems/binary-search-tree-iterator/

### Beats 94% of time complexity submissions. 
### O(H) space since we might store the height 
### O(1) amortized time complexity. O(H) time complexity when initialized, but then O(1) time complexity
### to pop and return smallest integer

### Two versions:
### Version N#1: Do in order traversal in __init__ with O(N) time in order to have the whole BST stored in 
### ascending order.
### Version N#2: The one below where only a left_search is done initially.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        # Run the function within initialization so that it finds the smallest integers in order 
        self.left_most_inorder(root)
        
    
    def left_most_inorder(self, root):
        
        # Keep going down the path to the left and add them into a stack, which means that you'll be 
        # removing them from the end, not from the beginning of the queue
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        stackLength = len(self.stack)
        # If there is another integer in the stack, then we haven't iterated through all numbers
        if stackLength > 0:
            smallestInteger = self.stack.pop() # Removes and returns last element of array
            # If the element we just popped has right children, we need to process them before it's parent element
            # since they are smaller. 
            # Run the function again on it's right child
            if smallestInteger.right:
                self.left_most_inorder(smallestInteger.right)
            return smallestInteger.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        stackLength = len(self.stack)
        return stackLength > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()