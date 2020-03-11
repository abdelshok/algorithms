### Easy-Medium
### Problem: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such
### that adding up all the values along the path equals the given sum.
### https://leetcode.com/problems/path-sum/

### Beats 98% submissions
### O(N) time complexity, O(D) space complexity where D is the maximum depth of the tree

class Solution(object):
    def hasPathSum(self, root, sumOne):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = self.hasPathSumHelper(root, sumOne, 0)
        return result
    
    def hasPathSumHelper(self, root, sumOne, cumulativeSum):
		# Can return 0 or False here, just need to make sure it returns
        if root is None:
            return False
		# If it's not none, then we add node's current value to cumulative sum
        else:
            cumulativeSum += root.val
            
        # Add the two other and statement to ensure that we are at a leaf node
        # Without it, it might return true for a path that doesn't end at the
        # leaf node
        if cumulativeSum == sumOne and root.left is None and root.right is None:
            return True
        
        # If one of the sub-branches has a cumulative sum equal to the one we're
        # looking for, then we return True
        # Ensures that we return True all the way to the top
        if self.hasPathSumHelper(root.left, sumOne, cumulativeSum) == True or self.hasPathSumHelper(root.right, sumOne, cumulativeSum) == True:
            return True
        else:
            return False
            