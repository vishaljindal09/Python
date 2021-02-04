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

"""
Two-pass Hash Table
To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

We reduce the look up time from O(n)O(n) to O(1)O(1) by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred, a look up could degenerate to O(n)O(n) time. But look up in hash table should be amortized O(1)O(1) time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement (target - nums[i]target−nums[i]) exists in the table. Beware that the complement must not be nums[i]nums[i] itself!

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_ds = { i : i for i in nums }
        
        for i in range (0, len(nums)):
            current_value = nums[i]
            value_needed = target - current_value
            
            
            if value_needed in hash_ds:
                index_key = list(hash_ds.keys()).index(value_needed)
                if index_key  != i:
                    result = [i,index_key]
                    return result
                
        
