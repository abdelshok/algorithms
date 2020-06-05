### Range Sum BST
### Problem: Given the root node of a binary search tree, return the sum of values of all nodes with value
### between L and R (inclusive)
### https://leetcode.com/problems/range-sum-of-bst/

### Beats 96% of time-complexity submissions 
### Here implemented with iterative breadth search search.

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        # BST has only unique values. It is a BST so smaller values on left
        # larger values on right
        # Easy question to key here is to optimize
        # If the node we're at is smaller, we only go check it's right values
        # If node is equal,then add, and go to the right
        # If node is within, just add it
        # If node is larger, then only add the right
        # If node is equal, then add and go to left
        
        queue = [root]
        total = 0
        
        while len(queue) > 0:
            removedNode = queue.pop()
            value = removedNode.val
            
            if value > L and value < R:
                total += value
                
                if removedNode.right:
                    queue.append(removedNode.right)
                    
                if removedNode.left:
                    queue.append(removedNode.left)
                    
            elif value <= L:
                if value == L:
                    total += value
                if removedNode.right:
                    queue.append(removedNode.right)
                # Do not append left node, as they are all smaller
            elif value >= R:
                if value == R:
                    total += value
                if removedNode.left:
                    queue.append(removedNode.left)
                # Do not append the right
                
        return total