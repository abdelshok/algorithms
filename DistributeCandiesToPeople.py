### Easy 
### Problem: We distribute some number of candies, to a row of n = num_people people in the following way:
### We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies
### to the last person.
### https://leetcode.com/problems/distribute-candies-to-people/

### Beats 95% of submissions for time complexity and 100% for space complexity
### O(N) time complexity where N is num_people, O(P


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # Keep going until we reach the end of array
        # When we reach the end of the array, we reset the index to 0 to start again
        # If we're not at the end of index, then we simply increment i by 1 
        # Keep count so that we know how much we add
        # If count <= remainingCandies, then we add the count
        # If count > remainingCandies, then we add the candies count
        count = 1
        index = 0
        peopleArray = [0] * num_people
        
        while candies > 0:
            if count < candies:
                peopleArray[index] += count
                candies -= count # Decrement the amount of candies by the count
                count += 1 # Increment the count
            else:
                peopleArray[index] += candies
                candies -= candies # Sets it to 0 and allows us to get out of loop 
                break
                
            index = 0 if (index == num_people-1) else index + 1
        
        return peopleArray
    
    
                