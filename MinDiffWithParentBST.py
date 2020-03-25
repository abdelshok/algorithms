### Easy: Minimum Distance Between BST Node and it's parent
### Problem: As the title suggests, a twist on the Leetcode exercise below.
### https://leetcode.com/problems/minimum-distance-between-bst-nodes/

### O(N) time complexity, O(H) space complexity
### No percentages to compare to other algorithms being that this is a self-created problem.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.minimum = float('inf')
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Actually when we hit leaf nodes, we return the integer
        # And in the top, we calculate the min between the two child nodes
        # And compare it to each other and current min until we get to top / root
        # node
        self.minDiffHelper(root)
        return self.minimum
    
    def minDiffHelper(self, node):
        # In case we ever get an empty root
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return node.val
        
        leftDiff = abs(self.minDiffHelper(node.left)-node.val) if node.left else float('inf')
        rightDiff = abs(self.minDiffHelper(node.right)-node.val) if node.right else float('inf')
        
        currMin = min(leftDiff, rightDiff)
        self.minimum = min(currMin, self.minimum)
        
        return node.val            
        