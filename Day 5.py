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


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # create a sorted enumarted list based on key as the element in list
        nums_new = sorted(list(enumerate(nums)), key=lambda x: x[1], reverse=True)
        # return the index positiion of the largest number
        return nums_new[0][0]


nums = [3, 30, 34, 5, 9]
func = Solution()
print(func.largestNumber(nums))
