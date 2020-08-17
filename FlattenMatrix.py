### Medium: Flatten Matrix 
### Ie. [[4,5], [112, 43], [], [3,4,5]] --> [4,5,112,43,3,4,5]
### Use an iterator that has the .next() method to return the next element
### and hasNext() which returns a boolean as to whether there's a next element in the matrix
### 

### O(NxM) Time complexity if N ≠ M. We could also say O(N) time complexity for N elements in 
### the array
### O(1) Space complexity


class Matrix(object):
    
  def __init__(self, matrix):
    self.outer = 0
    self.inner = 0
    self.matrix = matrix 
    self.matrixLength = self.findMatrixLength(matrix)
    self.rowLengths = self.findRowLengths(matrix)
    self.moveToNext(matrix, self.outer, self.inner)

  def moveToNext(self, vector, outer, inner):
    # Continuously keeps moving forward if there is a number
    # of empty arrays
    while self.outer < self.matrixLength and self.inner >= self.rowLengths[self.outer]:
      self.outer += 1 # Increment the outer by one 
      self.inner = 0 # Reset the inner pointer to be 0
      

  def findMatrixLength(self, matrix):
    return len(matrix)

  def findRowLengths(self, matrix):
    arrayOfRowLengths = []
    # O(N) or O(MxN) time complexity, however you want to look at it
    for i in range(self.matrixLength):
      currentRow = self.matrix[i]
      lengthRow = len(currentRow)
      arrayOfRowLengths.append(lengthRow)

  def nextNum(self):
    # Store the current number
    currentNumber = self.matrix[self.outer][self.inner]
    # Increment the inner so that next time we call the iterator 
    # we have it
    self.inner += 1 
    # Move the number ahead if there is nothing
    self.moveToNext(self.vector, self.outer, self.inner)
    return currentNumber

  def hasNext(self):
    return self.outer < self.matrixLength and self.inner < self.matrix[self.outer]



