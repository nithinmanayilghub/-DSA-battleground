# 274. H-Index
## https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1)
        for c in citations:
            paper_counts[min(c, n)] += 1

        h = n
        papers = paper_counts[n]
        while papers < h:
            h -= 1
            papers += paper_counts[h]
        return h


#####################################################################################################
# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
## 6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res
