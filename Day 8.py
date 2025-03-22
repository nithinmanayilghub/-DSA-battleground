#################################################### DAY 8 ########################################################
## Question 1 Jump Game
### https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
# Use Greedy Approach
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # initialize the goal as the last index of the list
        goal = len(nums) - 1
        # Start a loop in which we iteratively move the right pointer from right to left
        for i in range(len(nums) - 1, -1, -1):
            # check if the sum of the index of the right pointer and its value is greater than or equal to the goal
            if i + nums[i] >= goal:
                # Update the goal as the current index of the right pointer
                goal = i
        return True if goal == 0 else False


nums = [3, 2, 1, 0, 4]
func = Solution()
print(func.canJump(nums))

nums = [2, 3, 1, 1, 4]

func = Solution()
print(func.canJump(nums))


##########################################################################################################################################################################
## 322. Coin Change
### https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=array
## Approach - Dynamic Programming - Bottom up approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


nums = [1, 2, 5]
amount = 11
func = Solution()
print(func.coinChange(nums, amount))
