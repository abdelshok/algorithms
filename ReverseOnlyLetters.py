### Easy: Reverse Only Letters
### Given a string S, return the 'reversed" string where all characters
### that are not a letter stay in the same place, and all t
### https://leetcode.com/problems/reverse-only-letters/

### Beats 100% time complexity, 14% space complexity. Why is that.

### O(1) space complexity, O(N) time complexity

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Split into array
        # Go at both ends
        # If both letters, exchange them
        # If one not letter, increment or decrement until letter is found
        # If neither letters, then increment or decrement until letter is found or until 
        # they cross each other
        # Join them again
        # Return
        alphabet = list(string.ascii_letters)
        dictAlphabet = transform_into_dict(alphabet)
        stringArray = transform_into_array(S)
        length = len(stringArray)
        i, j = 0, length-1
        
        while i < j:
            leftChar, rightChar = stringArray[i], stringArray[j]
            if leftChar in dictAlphabet and rightChar in dictAlphabet:
                stringArray[i], stringArray[j] = rightChar, leftChar
                i, j = i+1, j-1 # Don't forget to increment and decrement them 
                # respectively
            else:
                if leftChar in dictAlphabet and rightChar not in dictAlphabet:
                    j -= 1
                elif leftChar not in dictAlphabet and rightChar in dictAlphabet:
                    i += 1
                else: 
                    i, j = i+1, j-1 # If they're both not characters of the alphabet
        
        finalString = ''.join(stringArray)
        return finalString
    
def transform_into_dict(iterable):
    dictAlphabet = {}
    for char in iterable: 
        dictAlphabet[char] = 1
    return dictAlphabet


def transform_into_array(string):
    arr = []
    for char in string:
        arr.append(char)
    return arr

