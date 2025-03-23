############################################DAY - 2#####################################################

# Question - 3 Length of last word
# Given a  sentence with words and sentences. find the length of the last word

s = " Learn Python "


def length_last_word(s: str) -> int:
    # Use a list comprehension to create a new list devoid of blank characters
    new_s = [w for w in s.split(" ") if w != ""]
    # calculate the length of last word in the new list
    len_last_w = len(new_s[-1])
    # return the length
    return len_last_w


s = "coding is fun"
print(length_last_word(s))

s = " fly me to the moon "
print(length_last_word(s))

##########################################################################################################

# Question - 4

## Given an array of integers sorted in non- decreasing order find the starting  and ending position of a given target value
from typing import List

nums = [5, 7, 7, 8, 8, 10]
target = 8


def find_start_end_pos(nums: List[int], target=int) -> List[int]:
    # Create a list to accumulate index positions
    res = []
    # Loop through the list of numbers
    for i, n in enumerate(nums):
        # Check if nums equal target if yes append the index position to result
        if nums[i] == target:
            res.append(i)
    # Check if the final result is an empty list. if yes return [-1]
    if res == []:
        return [-1, -1]
    return res


print(find_start_end_pos(nums, target))

nums = [5, 7, 7, 8, 8, 10]
target = 6

print(find_start_end_pos(nums, target))

nums = []
target = 0

print(find_start_end_pos(nums, target))


########################## EFFICIENT SOLUTION ################################################
def length_last_word(s: str) -> int:
    words = (
        s.strip().split()
    )  # `strip()` removes leading/trailing spaces, `split()` tokenizes words
    return len(words[-1]) if words else 0  # Handle case where words list is empty


s = " fly me to the moon "
print(length_last_word(s))

########

from typing import List
import bisect


def find_start_end_pos(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    left = bisect.bisect_left(nums, target)  # Find leftmost index of target
    right = bisect.bisect_right(nums, target) - 1  # Find rightmost index

    if left <= right and 0 <= left < len(nums):
        return [left, right]
    return [-1, -1]


# Test cases
nums = [5, 7, 7, 8, 8, 10]
print(find_start_end_pos(nums, 8))  # Output: [3, 4]

nums = [5, 7, 7, 8, 8, 10]
print(find_start_end_pos(nums, 6))  # Output: [-1, -1]

nums = []
print(find_start_end_pos(nums, 0))  # Output: [-1, -1]
