################################################DAY -3###############################################################
# Question 1 - Product of Array except itself
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the prefix and post fix
        prefix, postfix = 1, 1
        # Initialize an array of 1 with same length as of original array
        res = [1] * (len(nums))

        # loop though the new array and insert cumulative prefix product  in the corresponding index positions
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Loop through new array starting from the right and insert cumulative postfix product in the corresponding position
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


#########################################################################################################################################################################################
# Question 2 - Longest substring array
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize the left pointer as zero
        l = 0
        # Initialize the resuts ad Zero
        res = 0
        # Initialize the Charset to add all unique element sin string
        charset = set()
        # loop and remove element if it is a duplicate  in charset
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                # increment left pointer by 1
                l += 1
            # add the new element to the set
            charset.add(s[r])
            # max value of the window as  the result
            res = max(res, r - l + 1)
        return res


#############################################################################################
