"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
""" Brute force method

Time complexity : O(n^2). For each element, we try to find its complement by looping through the rest of array which takes O(n)O(n) time.
Therefore, the time complexity is O(n^2).

Space complexity : O(1).

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums)):
            current_value = nums[i]
            
            for j in range (i+1, len(nums)):
                value_needed = target - current_value
                
                if nums[j] == value_needed:
                    result = [i,j]
                    
        return result
