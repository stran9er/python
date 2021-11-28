'''
    Maximum Sum Subarray:
        Given an input that may contain + and - int, find the sum of 
        continous subarray of n which has largest sum.
'''
from typing import List

class MaxSumSubarray:
    def maxSumSub(self, nums: List[int]) -> int:

        # Variable to index our subarray
        maxSum = nums[0]

        for i in range (len(nums)):
            # Variable to hold our sum.
            sum = 0
        
        # Select each possible last index of the subarray
        for j in range (i, len(nums)):
            sum += nums[j]
            # we need to update maxSum to reflect sum of the subarray.
            maxSum = max(maxSum, sum)

        return maxSum

n = [-2, -5, 6, -2, -3, 5, -6]
my_array = MaxSumSubarray()
my_array.maxSumSub(n)
