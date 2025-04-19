## https://leetcode.com/problems/remove-k-digits/description/?envType=problem-list-v2&envId=greedy
# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # initailize stack
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        stack = stack[: len(stack) - k]
        res = "".join(stack)
        return str(int(res)) if res else "0"


####################################################################################
## 134. Gas Station
## https://leetcode.com/problems/gas-station/description/?envType=problem-list-v2&envId=greedy
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1
        return start
