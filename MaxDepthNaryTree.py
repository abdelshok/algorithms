### Easy
### Max Depth N-ary Tree
### Return the maximum depth of an n-ary given tree
### Link: 

### O(N) time complexity, O(W) space complexity where W is maximum width 
### of the tree
### 97% time submission, better than 100% of space submissions

### Iterative Solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # Recursive solution DFS 
        # Iterative solution DFS, track max
        maximum = float('-inf')
        queue = []
        
        if root is None:
            return 0
        else:
            queue.append([root, 1])
            
            while len(queue) > 0:
                removedVector = queue.pop()
                currNode = removedVector[0]
                currLevel = removedVector[1]
                childLength = len(currNode.children)
                
                if childLength != 0:
                    # Loop through children & add them
                    for childNode in currNode.children:
                        queue.append([childNode, currLevel+1])
                else: # No childen, hit a leaf node
                    maximum = max(currLevel, maximum)
                    
            return maximum
                
### Recursive Solution can also be implemented
