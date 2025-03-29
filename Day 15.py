########################################## DAY 15 ###############################################
## Find Permutation
## A permutation perm of n integers of all the integers in range [1,n] can be represented
## as a string  s of length n-1 where
## s[i] == "i" if perm[i] < perm[i+1]
## s[i] == "D" if perm[i] < perm[i+1]
## Given a string s, reconstruct lexicographically smallest permutation perm and return it
## Example - 1
## Input s = "I"
## OUTPUT = [1,2]
## Explanation [1,2] is the only legal permutation that can be represented by s,
## where the number 1 and 2 constuct an increasing relationship

## Example -2
## Input s = "DI"
## Output = [2,1,3]
## Explanation Both [2,1,3] and [3,1,2] can be represented as "DI",but since we want
## the smallest lexicographical permutation, you should return [2,1,3]
## "IDDI" = 1,4,3,2,5
## "IDDD" = 1,5,4,3,2
## Approach Use stack
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # Initialize empy list
        ans = []
        # Initialize empty list
        stack = []
        # start a loop to append  the list of numbers
        for i, c in enumerate(s):
            stack.append(i + 1)

            # check if the string letter is I
            if c == "I":
                # start a loop and append the numbers in ascening order
                while stack:
                    ans.append(stack.pop())

        # Other wise append the last digit
        stack.append(len(s) + 1)
        # start a loop and append the the digits
        while stack:
            ans.append(stack.pop())
        return ans


func = Solution()
s = "DI"
print(func.findPermutation(s))


############################################################################################
## 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create an empty dictionary
        count = {}
        # Initialize result as  zero
        res = 0
        # Initialize left pointer as zero
        l = 0
        # Initialize max value as zero
        maxf = 0

        # Start the loop for right pointer
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(count[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


func = Solution()
s = "ABAB"
k = 2
print(func.characterReplacement(s, k))
