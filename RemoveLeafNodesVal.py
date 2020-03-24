### Medium: Delete Leaves with A Given Value
### Problem: Given a binarty tree root adn an integer target, delete all the leaf nodes with
### value target. Onceyou delete a leaf node with value
### https://leetcode.com/problems/delete-leaves-with-a-given-value/submissions/

### Beats 95% submissions for time complexity, 100% submisison for space complexity
### O(N) time complexity, O(H) space complexity with H being max height of tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        newRoot = self.removeLeafNodeHelper(root, target)
        return newRoot
    
    def removeLeafNodeHelper(self, root, target):
        if root.left:
            root.left = self.removeLeafNodeHelper(root.left, target)
        if root.right:
            root.right = self.removeLeafNodeHelper(root.right, target)

        if root is None:
            return None
        # We add the two extra conditions to ensure that we only delete the leaf node
        elif root.val == target and root.left is None and root.right is None:
            return None

        return root