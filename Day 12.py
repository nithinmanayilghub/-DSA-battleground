#################################################### DAY 12##########################################################
## Maximum Consecutive ones
##   Given a binary array nums, return the maximum number of consecutive 1's in the array if
#### you can flip at most one 0
## Example - 1
# nums = [1,0,1,1,0]
# output = 4
##### Explanation
##### - If we flip the first zero, nums become [1,1,1,1,0] we have 4 consecutive ones
##### - If we flip second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones

## Example 2
## Input: nums = [1,0,1,1,0,1]
## output 4
## Explanation
## If we flip first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones
## If we flip second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize left and right pointer
        left, right = 0, 0
        # Initailize max window size
        max_window = 0
        # keep track of count of zeros
        zeros = 0

        # start a loop for right pointer
        while right < len(nums):
            # check if the elemnt is zero
            if nums[right] == 0:
                # increment zero count by 1
                zeros += 1
            # check if zero count is zero
            while zeros == 2:
                # check if the element at the left pointer is zero
                if nums[left] == 0:
                    # decrement the count of zeros by 1
                    zeros -= 1
                # increment left pointer by 1
                left += 1
            # calculate maximum window size
            max_window = max(max_window, right - left + 1)
            # increment right pointer by 1
            right += 1

        return max_window


nums = [1, 0, 1, 1, 0, 1]
func = Solution()
print(func.findMaxConsecutiveOnes(nums))


#####################################################################################################################################
## 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
