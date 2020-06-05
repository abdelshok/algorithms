### Easy: Average of levels
### Problem: Return array that contains the average of each level of binary tree
###

### Beats 77% of time complexity submissions. Very weak.
### O(N) time, O(N) space

### Initial Version


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Do level order traversal, keep adding to the last element array if same level
        # Keep track of counter so that when you reach a new level
        # You divide the last element by the counter
        # Don't forget to divide the last element after the loop is over
        
        if root is None:
            return []
        else:
            levels = getLevelArray(root)
            length = len(levels)
            
            for i in range(length):
                level = levels[i]
                levels[i] = sum(level)/float(len(level))
            
            return levels
            
def getLevelArray(node):
    queue = [[node,0]]
    currLevel = -1
    finalLevel = []

    while len(queue) > 0:
        removedNode = queue.pop(0)
        nodeLevel = removedNode[1]
        nodeVal = removedNode[0].val


        if currLevel == nodeLevel:
            # If same level, then simply add it to the 
            lastArray = finalLevel[-1]
            lastArray.append(nodeVal)
        else:
            # If nodes not same level
            finalLevel.append([nodeVal]) # Add new array for that level
            # Don't forget to increment the current level
            currLevel += 1 

        if removedNode[0].left:
            queue.append([removedNode[0].left, nodeLevel+1])
        if removedNode[0].right:
            queue.append([removedNode[0].right, nodeLevel+1])
    
    return finalLevel


### Counter version
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # Do level order traversal, keep adding to the last element array if same level
        # Keep track of counter so that when you reach a new level
        # You divide the last element by the counter
        # Don't forget to divide the last element after the loop is over
        
        if root is None:
            return []
        else:
            levels = getLevelArray(root)
            length = len(levels)
        
            return levels[1:] # Kind of a hack here.
            
def getLevelArray(node):
    queue = [[node,0]]
    totalSum = node.val
    count = 1
    currLevel = -1
    averageArray = []

    while len(queue) > 0:
        removedEl = queue.pop(0)
        removedNode = removedEl[0]
        nodeLevel = removedEl[1]
        nodeVal = removedNode.val

        if currLevel == nodeLevel:
            # Add to the total sum the value and increment count
            totalSum += nodeVal
            count += 1
        else:
            # If nodes not same level, different things we have to do
            # 1. Store the total sum in the finalLevel array divided by the count
            # 2. Reset the count to 1 so that we can start with the new
            # 3. Increment currLevel by 1 
            averageArray.append(totalSum/float(count))
            totalSum = nodeVal
            count = 1
            currLevel += 1

        if removedNode.left:
            queue.append([removedNode.left, nodeLevel+1])
        if removedNode.right:
            queue.append([removedNode.right, nodeLevel+1])
    
    averageArray.append(totalSum/float(count))
    
    return averageArray