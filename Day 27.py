# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=array
# 42. Trapping Rain Water

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


#################################################################################################################################
### https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=array
## 128. Longest Consecutive Sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


func = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(func.longestConsecutive(nums))
