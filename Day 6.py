# Longest substring with atmost two distinct characters
# Given a string s, find the length of the longest substring t that contains at most 2 distinct characters

# s = "eceba"
# # output :3
# s = "ccaabbb"
# # output : 5


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # initialize left pointer as zero
        start = 0
        # initialize right pointer as zdero
        end = 0
        # initialize the max-length of the string with atmost 2 distinct characters
        max_len = 0
        # initialize a dictionary to keep track of the index
        d = {}
        # loop through the string with atmost 2 characters
        while end < len(s):
            # store the character and corresponding index in the dictionary
            d[s[end]] = end
            # if len of the dictionary is greater tahn 2
            if len(d) > 2:
                # find the minimum index
                min_ind = min(d.values())
                # increment the left pointer by one
                start = min_ind + 1
                # delete the minimum index
                del d[s[min_ind]]
            # Keep trakc of the maximum length
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len


###################################################################################################
# 516. Longest Palindromic Subsequence


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for i in range(len(s) + 1)]
        res = 0
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res

        cache = {}

        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                length = 1 if i == j else 2
                cache[(i, j)] = length + dfs(i - 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
            return cache[(i, j)]

        for i in range(len(s)):
            dfs(i, i)
            dfs(i, i + 1)
        return max(cache.values())


#################################################################################################################
