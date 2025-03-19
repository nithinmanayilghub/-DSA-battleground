################################################## DAY - 5 ##########################################################################
### 179. Largest Number
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Loop through the enumerated list of numbers
        for i, n in enumerate(nums):
            # convert each number in the list to a string
            nums[i] = str(n)

        # define a fucntion named compare whcih returns -1 and 1
        def compare(n1, n2):
            # returns -1 if first digit is greater in first position results in a larger number
            if n1 + n2 > n2 + n1:
                return -1
            # returns 1 if the second digit in the first position results in a larger number
            else:
                return 1

        # sort the list based on the compare function
        nums = sorted(nums, key=cmp_to_key(compare))
        # convert to int to eliminate precededing zeros if any and then again convert back to string
        return str(int("".join(nums)))


nums = [3, 30, 34, 5, 9]
func = Solution()
print(func.largestNumber(nums))

##############################################################################################
### 162. Find Peak Element

from typing import List


# Use binary search for finding  the peak value
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            # search the left neighbors if the left element is larger than middle element
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            # search the right neighbors if the right element is larger than middle elemnt
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
