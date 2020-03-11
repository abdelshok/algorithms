### Medium
###G iven a binary tree containing digits from 0-9 only, each root-to-leaf path 
### could represent a number. An example is the root-to-leaf path 1->2->3 which 
### represents the number 123. Find the total sum of all root-to-leaf numbers.
### https://leetcode.com/problems/sum-root-to-leaf-numbers/

### Beats 86% of submissions
### O(N) time complexity, O(D) space complexity where D is maximum depth
### Remember:
### 1. Find all of conditions of when to stop. When to stop and add no value and when
### to stop and value
### 2. First none, then check if correct value, then check children and recurse
### accordingly

class Solution(object):
    def __init__(self):
        self.sum = 0
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Brute force is to store all paths from root to leaf node into 
        # an array. Then we loop through the array and join each element 
        # (number) and add them to a cumulative total initially set to 0
        # ie. pathsArray = [[1,2], [1,3]] --> loop through it and +12 and
        # +13 for a total 25
        # Time complexity: O(N) + O(x+y) where x is the average number of 
        # numbers in each elements in pathsArray and y the number of path from 
        # root to leaf (which is the number of elements in pathsArray)
        # Space complexity O(D) where D is maximum depth
        
        # Let's find an O(N) solution
        self.sumNumberHelper(root, '')
        return self.sum
    
    def sumNumberHelper(self, node, string):
        # If node is None, return empty string
        if node is None:
            return ''
    
        # If both children are None then we hit a leaf, add the last value
        # to the string of numbers, convert that final number to an integer
        # and add it to sum
        if node.left is None and node.right is None:
            string = string + str(node.val)
            self.sum += int(string)
        
        # No need to call the function if children is None
        if node.left is not None:
            self.sumNumberHelper(node.left, string+str(node.val))
        if node.right is not None:
            self.sumNumberHelper(node.right, string+str(node.val))


#############################

### Other solution from someone else, pretty good although the naming
### of the variables isn't so great. numString would be better than num

class Solution(object):
    def sumNumbers(self, root):
        
        if not root:
            return 0
        
        ls = []
        
        def dfs(root,num):

            if root:
                num += str(root.val)
                if not root.left and not root.right:
                    ls.append(int(num))
                    return 
                dfs(root.left,num)
                dfs(root.right,num)

        
        dfs(root,"")
        
        return sum(ls)