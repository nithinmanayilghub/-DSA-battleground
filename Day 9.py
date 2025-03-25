############################################## DAY 9 ###############################################################
## https://leetcode.com/problems/find-k-closest-elements/description/?envType=problem-list-v2&envId=sorting
## 658. Find K Closest Elements
## Approach Use twopointers and binary search
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize the left and right pointer
        l, r = 0, len(arr) - k
        # start a loop for binary search
        while l < r:
            # calculate the middle value
            m = (l + r) // 2
            # check if the difference between x and middle element is greater than difference between element after the window and x
            if x - arr[m] > arr[m + k] - x:
                # if yes increment left pointer as midpoint + 1
                l = m + 1
            else:
                # if no change the right pointer to mid point
                r = m
        return arr[l : l + k]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
func = Solution()
print(func.findClosestElements(arr, k, x))


#######################################################################################################
## 522. Longest Uncommon Subsequence II
## https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/?envType=problem-list-v2&envId=sorting
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub_seq(s1, s2):
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == len(s1)

        n = len(strs)
        ans = -1
        for i in range(n):
            valid = True
            for j in range(n):
                if i == j:
                    continue
                if is_sub_seq(strs[i], strs[j]):
                    valid = False
                    break
            if valid:
                ans = max(ans, len(strs[i]))
        return ans


func = Solution()
strs = ["aba", "cdc", "eae"]

print(func.findLUSlength(strs))

"""
Simulate what's going on inside the code using the exmaple input. 
The goal is to undersand what happens at each line of code on a given Input. 
Print the output for an absolute beginner
"""
