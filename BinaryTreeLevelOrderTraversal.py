### Medium
### Problem: Print level order traversal of BST ie. [[5], [3, 6], [1, 8, 9]]
### https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

### Beats 96% of submissions for time complexity
### O(N) time complexity, O(N) space complexity

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Iterate and keep track of current level
        # Check level of current node we're removing
        # If same level then we append it to the last array
        # If diff level, then we create an array with it inside 
        # and append it
        # Should be O(N) time complexity, O(N) space complexity
        
        levelOrderArray = []
        currentLvl = -1
        queue = [[root, 0]]
        
        if root:
            while len(queue) > 0:
                removedNodeEl = queue.pop(0) # Removes left most element
                node = removedNodeEl[0]
                nodeLevel = removedNodeEl[1]

                if node.left:
                    queue.append([node.left, nodeLevel+1])
                if node.right:
                    queue.append([node.right, nodeLevel+1])

                if nodeLevel != currentLvl: # Then we encountered the first element
                    # of the next level
                    # Create array with value that we add
                    levelArr = [node.val]
                    levelOrderArray.append(levelArr)
                    currentLvl += 1 # Increment current level
                else: 
                    # We're still on same level
                    lastArr = levelOrderArray[-1]
                    lastArr.append(node.val)

            return levelOrderArray
        else:
            return []
            
            