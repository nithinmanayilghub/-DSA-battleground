# 122. Best Time to Buy and Sell Stock II
## https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=problem-list-v2&envId=greedy
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize Profit variable
        profit = 0
        # start a loop to iterate through the list
        for i in range(1, len(prices)):
            # check if the current value is greater than previous value
            if prices[i] > prices[i - 1]:
                # Update the profit
                profit += prices[i] - prices[i - 1]
        return profit


###################################################################################################
## 334. Increasing Triplet Subsequence
## https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_i = num_j = float("inf")
        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False


func = Solution()
nums = [1, 2, 3, 4, 5]
print(func.increasingTriplet(nums))
