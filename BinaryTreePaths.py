### Easy
### Problem: Given a binary tree, return all root to leaf paths in the form: ["1->4->5", "1->10"]
### https://leetcode.com/problems/binary-tree-paths/

### Beats 96% of submissions for time complexity
### O(B) space complexity where B is the number of paths, O(N) time complexity

### Advice: remember to look the clues in the question itself, told you what the terminal constraint was
### More importantly, remember that appending when the node is None (after we iterate on empty leaves)
### means that we append the data twice, making the output erroneous. Sometimes appending / returning
### data values after checking if children exist at all is better


class Solution(object):
    def __init__(self):
        self.allPaths = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.findAllRootPaths(root, '')
        return self.allPaths
    
    def findAllRootPaths(self, root, string):
        if root is None:
            # Actually we simply add the string to the array because it means
            # we've passed a leaf node
            return
        
        if string == "":
            string = str(root.val)
        else:
            string = string + "->" + str(root.val) # Adds the element to the string
        
        if root.left is not None:
            self.findAllRootPaths(root.left, string)
        if root.right is not None:
            self.findAllRootPaths(root.right, string)
        
        if root.right is None and root.left is None:
            self.allPaths.append(string)
        
        