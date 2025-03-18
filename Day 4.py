########################################## DAY - 4 ##############################################################
# 209. Minimum Size Subarray Sum
from typing import List


# Use the Sliding Window technique to keep track of minimum length of array that sum to target
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the left pointer and total sum as zeros
        l, total = 0, 0

        # Initialize the length of the result array as infinity
        res = float("inf")

        # Start a loop for the rightpointer
        for r in range(len(nums)):
            # add the element corresponding to the right pointer to the total
            total += nums[r]
            # check whether the total sum is greater than or equal to the target
            while total >= target:
                # if the total is greater than or equal to the target
                res = min(r - l + 1, res)
                # remove the left most element from the total once the condition is met
                total -= nums[l]
                # increment the leftpointer by 1
                l += 1

        return 0 if res == float("inf") else res


# nums = [2, 3, 1, 2, 4, 3]

# target = 7

# func = Solution()
# print(func.minSubArrayLen(target, nums))

##################################################################################################
# 1984. Minimum Difference Between Highest and Lowest of K Scores


# Here also  we use the sliding window technique on the sorted array
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sort the array in ascending order, so that adjacent values have minimum difference
        nums.sort()
        # Initialize the left and right pointers
        l, r = 0, k - 1
        # Initialize the result as infinity which inturn is our minimum difference in the beginning
        res = float("inf")
        # loop through the  sorted array and caculate the difference between adjacent elements
        while r < len(nums):
            diff = nums[r] - nums[l]
            # keep tack of the minimum difference value
            res = min(res, diff)
            # increment the left and right pointers by 1
            l, r = l + 1, r + 1
        return res


nums = [9, 4, 1, 7]
k = 2
func = Solution()
print(func.minimumDifference(nums, k))
