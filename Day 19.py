####################################### Day 19 ################################################
# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # create a list of words
        words = s.split(" ")
        # check if the length of pattern and the number of words are equal.
        if len(pattern) != len(words):
            return False
        # Initialize dictionary that maps character to word
        charToWord = {}
        # Intialize a dictionary that maps word to char
        wordToChar = {}
        # start a loop through a list of tuples of pattern and words
        for c, w in zip(pattern, words):
            # check if character is in the dictionary and if it maps to word correcly
            if c in charToWord and charToWord[c] != w:
                return False
            # check if word is in dictionary and if maps to character correctly
            if w in wordToChar and wordToChar[w] != c:
                return False
            # update the mapping of character of dictonary
            charToWord[c] = w
            # update the mapping of word to character
            wordToChar[w] = c
        return True


func = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(func.wordPattern(pattern, s))

########################################################################################
## 33. Search in Rotated Sorted Array
## Approach Modified Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointer
        l, r = 0, len(nums) - 1

        # start loop for modified binary search
        while l <= r:
            # calculate the middle index
            m = (1 + r) // 2
            # check if the middle index and target are equal
            if nums[m] == target:
                return m
            # check if the target is in the left sorted array
            if nums[l] <= nums[m]:
                if nums[l] < target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # check if the target is in the right sorted array
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
