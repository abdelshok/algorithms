### Google Onsite - Find Minimum Values of Sub-Matrix of size K
### Hard
### Given an n x m matrix and a value k, find minimum values for all sub-matrixes of size k
### Similar on Leetcode: https://leetcode.com/problems/sliding-window-maximum/

### Input
array = [
        [-1, 5, 4, 1, -3],
        [4,  3, 1, 1, 6],
        [2, -2, 5, 3, 1],
        [8,  5, 1, 9, -4],
        [12, 3, 5, 8, 1]
    ]

### Output 

finalArr = [
	[-2, -2, -3],
	[-2, -2, -4],
	[-2, -2, -4]
]

### Time complexity: O(M x N x K). Could be improved to O(MxN)
### Space complexity O(MxK)

### Personal comment: Greatest question that I've ever seen.

def subMatrix(k):
  width = len(array[0])
  length = len(array)
  firstArray = []
  finalArray = []

  for i in range(length-k+1):
    # Add new empty array
    firstArray.append([])
    for j in range(width):
      internalArray = firstArray[-1]
      internalArray.append(findVerticalMinimum(array, i, j, k))

  newLength = len(firstArray)
  newWidth = len(firstArray[0])

  for i in range(newLength):
    finalArray.append([])
    for j in range(width-k+1):
      internalArray = finalArray[-1]
      internalArray.append(findHorizontalMinimum(firstArray, i, j, k))

  print('Final array')
  print(finalArray)

  return finalArray

def findVerticalMinimum(array, i, j, k):
  minimum = float('inf')
  for l in range(k):
    minimum = min(minimum, array[i+l][j])
  return minimum

def findHorizontalMinimum(firstArray, i, j, k):
  minimum = float('inf')
  for l in range(k):
    minimum = min(minimum, firstArray[i][j+l])
    print(minimum)
  return minimum

subMatrix(3)
