#
# 1493. Longest Subarray of 1's After Deleting One Element
## https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # initialize max length as zero
        max_len = 0
        # initialize index of zero
        zero = -1
        # initailize start pointer
        start = 0
        # Loop through the array
        for i in range(len(nums)):
            # check if the element is zero
            if nums[i] == 0:
                # update the start pointer
                start = zero + 1
                # update the index of zero
                zero = i
                # find the maximum value
            max_len = max(max_len, i - start)
        return max_len


############################################################################################################
## 680. Valid Palindrome II
## https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Initialize left and right pointer
        l, r = 0, len(s) - 1
        # start a loop
        while l < r:
            # check if elememts at left and right pointer is equal
            if s[l] != s[r]:
                skipL, skipR = s[l + 1 : r + 1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1
        return True


s = "aba"
func = Solution()
print(func.validPalindrome(s))
