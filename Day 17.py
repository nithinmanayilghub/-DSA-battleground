######################################################### DAY 17###############################################################
## 1011. Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
from typing import List
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Initialize left and right pointer as maximum weight and sum of weights
        l, r = max(weights), sum(weights)
        # Initialize the result as right pointer
        res = r

        # define a funcation if sshipping a capacity is possible
        def canShip(cap):
            ship = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = cap
                currCap -= w
            return ship <= days

        # do binary search between the left and right pointer values
        while l <= r:
            cap = (r + l) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res


func = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(func.shipWithinDays(weights, days))


######################################################################################################################
## 2594. Minimum Time to Repair Cars
## https://leetcode.com/problems/minimum-time-to-repair-cars/description/


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, ranks[0] * cars * cars
        res = -1

        def count_repaired(time):
            count = 0
            for r in ranks:
                count += int((time / r) ** 0.5)
            return count

        while l <= r:
            m = (r + l) // 2
            repaired = count_repaired(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res


func = Solution()
ranks = [4, 2, 3, 1]
cars = 10
print(func.repairCars(ranks, cars))
