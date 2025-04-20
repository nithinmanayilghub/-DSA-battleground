## 670. Maximum Swap
## https://leetcode.com/problems/maximum-swap/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_digit = "0"
        max_i = -1
        swap_i = swap_j = -1
        for i in reversed(range(len(num))):
            # max
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i

            # swap
            if num[i] < max_digit:
                swap_i, swap_j = i, max_i
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int("".join(num))


num = 2736
func = Solution()
print(func.maximumSwap(num))


#######################################################################################################
# 881. Boats to Save People
## https://leetcode.com/problems/boats-to-save-people/description/?envType=problem-list-v2&envId=greedy
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res


people = [3, 2, 2, 1]
limit = 3
func = Solution()
print(func.numRescueBoats(people, limit))
