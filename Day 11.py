######################################### DAY 11 #########################################################
## 80. Remove Duplicates from sorted Array II
## https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=problem-list-v2&envId=two-pointers
from typing import List

### Approach - Two pointers


# class solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # Initialize second pointer on the second index
#         left = 2
#         # check if the total length of the list is less than or equal to 2
#         if len(nums) <= 2:
#             # if yes return True
#             return len(nums)
#         # Initialize the loop  for right pointer
#         for right in range(2, len(nums)):
#             # check if the number at right pointer not equal to the one two index before
#             if nums[right] != nums[right - 2]:
#                 # if not update the  left pointer by 1
#                 nums[l] = nums[right]
#                 # update the left pointer by 1
#                 left += 1
#         return left


########################################################################################################
## Question 22:
### Valid Word abbreviation
### String abbreviation - replace non-adjacent, non-empty substrings with their lengths. The lengths
### should not have leading zeros
### Given a string word and abbreviation abbr, return whether the string matches the given abbreviation
### A substring is a continguous non-empty
#### Example 1
##### Input: "internationalization",abbr = "i12iz4n" ("i nternational iz ation")
##### Output: true
#### Example 2
#### Input word = "apple", "abbr" = "a2e"
#### Output False
#### Explanation : apple = "a2e"
### https://youtu.be/Sut-F029biM
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                steps = 0
                if abbr[abbr_ptr] == "0":  # Leading zeros are not allowed
                    return False
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                word_ptr += steps
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                word_ptr += 1  # Correctly move both pointers when characters match
                abbr_ptr += 1
        return word_ptr == len(word) and abbr_ptr == len(abbr)


func = Solution()
word1 = "apple"
abbr1 = "a2e"
print(func.validWordAbbreviation(word1, abbr1))
word2 = "internationalization"
abbr2 = "i12iz4n"
print(func.validWordAbbreviation(word2, abbr2))
