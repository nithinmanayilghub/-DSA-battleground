#################################### DAY 20 ##################################################
## 216. Combination Sum III
## https://leetcode.com/problems/combination-sum-iii/description/?envType=problem-list-v2&envId=array
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def comb(curr, k, n, start):
            if k == 0 and n == 0:
                result.append(curr)
                return
            if k < 0:
                return
            for i in range(start, min(10, n + 1)):
                comb(curr + [i], k - 1, n - i, i + 1)
            return

        comb([], k, n, 1)
        return result


func = Solution()
k = 3
n = 7
print(func.combinationSum3(k, n))
#######################################################################################
## 318. Maximum Product of Word Lengths
## https://leetcode.com/problems/maximum-product-of-word-lengths/description/?envType=problem-list-v2&envId=array
from collections import defaultdict


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(set)
        for w in words:
            lookup[w] = set(w)

        mx = 0

        def dont_share(s, t):
            if lookup[s] & lookup[t]:
                return False
            return True

        for i in words:
            for j in words:
                if dont_share(i, j):
                    mx = max(mx, len(i) * len(j))
        return mx


func = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(func.maxProduct(words))
