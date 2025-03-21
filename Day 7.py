# Valid traingle
### https://leetcode.com/problems/valid-triangle-number/description/?envType=problem-list-v2&envId=sorting
# plan
# sort the array in the increasing order
# Initialize three pointers from right to left
# pointer a at right end
# pointer c at index one less than a
# pointer b at left end
# calulate all the possible triplets using numbers between b and c and a if the following
# condition is met b + c > a
# accumulate the result and print the result.

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for a in range(len(nums) - 1, 1, -1):
            b, c = 0, a - 1
            while b < c:
                if nums[b] + nums[c] > nums[a]:
                    res += c - b
                    c -= 1
                else:
                    b += 1
        return res


nums = [2, 2, 3, 4]
func = Solution()
print(func.triangleNumber(nums))


####################################################################################################
## 164. Maximum Gap
### https://leetcode.com/problems/maximum-gap/description/?envType=problem-list-v2&envId=sorting
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()
        # Initialize a variable for maximum difference
        max_diff = 0
        # initialize te left pointer as l
        l = 0
        # check if the length of array is  less than or equal to 1 if yes return 0
        if len(nums) <= 1:
            return 0
        # start the right pointer loop
        for r in range(1, len(nums)):
            # calculate the difference
            diff = nums[r] - nums[l]
            # keep track of maximum difference
            max_diff = max(max_diff, diff)
            # increment left pointer by 1
            l += 1
        # return maximum difference
        return max_diff


nums = [3, 6, 9, 1]
func = Solution()
print(func.maximumGap(nums))
