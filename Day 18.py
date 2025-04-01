############################################## Day 18 ####################################################################
# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/
### Approach Merge Intervals
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Initialize an empty list as result
        res = []
        # start a aloop to iterate through intervals
        for i in range(len(intervals)):
            # check if the second element of new interval is less than first element of the intervals. That means they are not overlapping
            if newInterval[1] < intervals[i][0]:
                # append the newInterval infront of the result
                res.append(newInterval)
                # append the remaining intervals
                return res + intervals[i:]
            # check if the first element comes after the last element in the interval non-overlapping
            elif newInterval[0] > intervals[i][1]:
                # add the inetrvals in order in the result
                res.append(intervals[i])
            else:
                # If the new Interval is overlapping the intervals. If yes update the new Interval with minimum and maximum terms.
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)

        return res


func = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(func.insert(intervals, newInterval))


##################################################################################################################
## 56. Merge Intervals
## https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the array
        intervals.sort(key=lambda i: i[0])
        # initialize first interval as output
        output = [intervals[0]]
        # start a loop to track start and end value of intervals
        for start, end in intervals[1:]:
            #  Track the end value of previous interval
            lastEnd = output[-1][1]
            # check if the start of the current interval is less than the previous interval's next
            if start <= lastEnd:
                # update the last intervals end as the maximum of current end and last interval's end
                output[-1][1] = max(lastEnd, end)
            else:
                # append the start and end of the interval
                output.append([start, end])
        return output


func = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(func.merge(intervals))
