### Hard
### Given a non-empty binary tree, find the maximum path sum.
### For this problem, a path is defined as any sequence of nodes from some starting node to any node in the
### tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
### https://leetcode.com/problems/binary-tree-maximum-path-sum/

### Beats 97% of submissions
### O(N) time complexity, O(D) space complexity where D is max depth
### Remember: 
### 1. Reset left or right sum to 0 if it is negative
### 2. Store curr max in global variable in case nodes that came
### before are negative
### 3. Return the max left or right path + value in case nodes above
### are positive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Make sure that it's -inf so even if all values
    # are negative we can find the minimum
    
    def __init__(self):
        self.maxSum = float('-inf')
        
    def maxPathSum(self, root):
        self.maxPathSumHelper(root)
        return self.maxSum
    
    
    def maxPathSumHelper(self, node):
        if node is None:
            return 0

        left = self.maxPathSumHelper(node.left)
        right = self.maxPathSumHelper(node.right)

        left = 0 if left < 0 else left
        right = 0 if right < 0 else right
        
        self.maxSum = max(left+right+node.val, self.maxSum) # Stores the highest value so we
        # can compare it later
        return max(left,right) + node.val
