####524. Longest Word in Dictionary through Deleting
## https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/?envType=problem-list-v2&envId=sorting
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def helper(sub, whole):
            N, M = len(sub), len(whole)
            i, j = 0, 0
            while j < M and i < N:
                if sub[i] == whole[j]:
                    i += 1
                j += 1
            return i == N

        # loop through helper
        output = ""
        for w in dictionary:
            if helper(w, s):
                output = min(output, w, key=lambda x: (-len(x), x))
        return output


#####################################################################################################
## https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=greedy
# 55. Jump Game


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
