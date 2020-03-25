### Easy: Minimum Distance Between BST Nodes
### Problem: Given a BST with the root node root, return the minimum difference
### between the values of any two different nodes in the tree
### 

### Beats 87-90% of submissions with time complexity, a lower in space complexity
### O(NlogN) time complexity because of sorting, O(N) space complexity

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.arr = []
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Traverse BST, store all values in array O(N) time, O(N) space
        # Sort array O(nLogN)
        # Loop through array and calculate diff between adjacent values O(N)        
        
        self.storeBSTValues(root)
        self.arr.sort()
        length = len(self.arr)
        minimum = float('inf')
        
        for i in range(length-1):
            # Minimum is minimum between the current minimum or the diff between
            # the two adjacent integers
            minimum = min(minimum, self.arr[i+1]-self.arr[i])
            
        return minimum
    
    # Pretty sure that post-order search will most likely store values closer 
    # to ascending order
    def storeBSTValues(self, node):
        if node is None:
            return None
        
        if node.left:
            self.storeBSTValues(node.left)
        if node.right:
            self.storeBSTValues(node.right)
            
        self.arr.append(node.val)


