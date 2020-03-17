### Easy
### Problem: Removed duplicates from sorted list
### https://leetcode.com/problems/remove-duplicates-from-sorted-list/

### Beats 94% of submissions
### O(N) time complexity, O(1) space complexity

### Advice: When it comes to pointers or linked list related problems like this, don't forget that
### errors arise in the while or for loops, when sometimes a node doesn't have a certain property
### because it is none. Ask yourself, what's the worst case scenario instead of asking yourself the
### best case scenario. In this case "1-->1-->1-->1-->1-->None" could have led to an error in the 
### internal while loop because you did not account for that possibility


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If both nodes are same, nextNode moves ahead until it is not the same value
        # as the currNode
        # When it's different value, we connect them, and then move both nodes forward
        # Move the currNode to where the nextNode is and nextNode one node further
        # We stop when the nextNode is None
        
        if head is None:
            return None
        else:
            currNode, nextNode = head, head.next
            while nextNode is not None:
                # Do something
                if nextNode.val != currNode.val:
                    # Move both forward
                    currNode = currNode.next
                    nextNode = nextNode.next
                else: # If they're the same, we move next node until it's different
                    while nextNode is not None and nextNode.val == currNode.val:
                        nextNode = nextNode.next
                    # When this is over, we connect them and therefore remove duplicates
                    currNode.next = nextNode
                    
                    # Now we move them both forward
                    currNode = currNode.next
                    nextNode = nextNode.next if nextNode is not None else None
                
            return head

            