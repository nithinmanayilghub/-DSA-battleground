######################################## DAY - 10 #########################################################
## 1291. Sequential Digits
## https://leetcode.com/problems/sequential-digits/description/

from typing import List
from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Initialize a list to keep track of List
        res = []
        # Initialize a queue with numbers of range 1 to 10
        queue = deque(range(1, 10))
        # Start a loop to loop through array
        while queue:
            # pop the left most element in the queue
            n = queue.popleft()
            # skip  if element exceeds high
            if n > high:
                continue
            # check if the popped element is with in low and high
            if low <= n <= high:
                # if yes append it to res
                res.append(n)
            # extract the last digit of the number
            ones = n % 10
            # append next sequential element if greater than 9
            if ones < 9:
                queue.append(n * 10 + (ones + 1))
        return res


func = Solution()
low = 100
high = 300
print(func.sequentialDigits(low, high))

#######################################################################################
## 523. Continuous Subarray Sum

## https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Initialize a remainder map to store remainders
        remainder = {0: -1}
        # Initialize total sum
        total = 0
        # Loop through nums
        for i, n in enumerate(nums):
            # update total sum
            total += n
            # compute the remainder
            r = total % k
            # If r is not the remainders' dictionary store it in it
            if r not in remainder:
                remainder[r] = i
            # check if r is previously in remainders' dictionary and check if sub array size is greater than 1
            elif i - remainder[r] > 1:
                return True
        return False


func = Solution()
nums = [23, 2, 4, 6, 7]
k = 6
print(func.checkSubarraySum(nums, k))
