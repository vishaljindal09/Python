"""
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.

 Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""

"""
Brute force with O(n^2),time limit excedd issues in leet code 18/19 test cases passed

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(0,len(numbers)):
            
            current_value = numbers[i]

            for j in range(i+1, len(numbers)):
                
                value_req = target - current_value
                
                if numbers[j] == value_req :
                    
                    result = [i+1,j+1]
                    
                    return result
                
                elif numbers[i] + numbers [j] > target :
                    
                    break
                    
      
      

"""

O(n) time complexity O(1) space 

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        
        while l<r:
            
            if numbers[l] + numbers[r] > target:
                
                r -= 1
                
            elif numbers[l] + numbers[r] < target:
                
                l +=1
            
            else:
                
                return [l+1, r+1]
        return
        
