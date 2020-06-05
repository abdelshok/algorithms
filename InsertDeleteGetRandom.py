### Insert Delete GetRandom O(1)
### Design a DS that supports all following operations in average O(1) time: insert, delete, getRandom
### https://leetcode.com/problems/insert-delete-getrandom-o1

### Beats 99% of submissions for time complexity
### O(1) time, O(N) space

class RandomizedSet(object):
    
    def __init__(self):
        self.hashTable = {}
        self.arr = []
        

    def insert(self, val):
        if val not in self.hashTable:
            self.arr.append(val)
            self.hashTable[val] = len(self.arr)-1
            return True
        return False
        

    def remove(self, val):
        if val in self.hashTable:
            index = self.hashTable[val]
            lastVal = self.arr[-1]
            self.arr[index] = lastVal # Move lastVal to position of value we want gone
            self.hashTable[lastVal] = index # Re set the new position of lastVal
            self.arr.pop() # Remove last val, which we just moved, to avoid duplicate
            del self.hashTable[val]
            return True
        
        return False
    
    def getRandom(self):
        return random.choice(self.arr)


