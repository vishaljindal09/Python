"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

problem break

sort and then duplicate can be skipped. Break 3 sum to 1+2. USe two sum for +2 value. Also there can be  many solutions so need to update pointer,
once 1 solution reached for the next solution with same starting number


time complexity O(nlogn) for sorting and o(n^2) for two loops
space o(n) (sorting)

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]: #duplicate needs to be skipped but continue loop
                continue
                
            l,r = i+1, len(nums)-1            
            while l < r:
                threesum = a + nums[l] + nums[r]            
                if threesum > 0:                    
                    r -=1                
                elif threesum < 0:                    
                    l +=1
                else:
                    res.append([a ,nums[l], nums[r]])
                    l +=1 #next solution
                    while nums[l] == nums[l-1] and l < r: #duplicate needs to be skipped
                           l +=1
        return res         
                 
