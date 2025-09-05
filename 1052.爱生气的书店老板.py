#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        current = 0
        for i in range(minutes):
            current += customers[i] if grumpy[i] == 1 else 0
        result = current
        result_left = 0
        for i in range(len(customers) - minutes):
            current += customers[i + minutes] if grumpy[i + minutes] == 1 else 0
            current -= customers[i] if grumpy[i] == 1 else 0
            if current > result:
                result = current
                result_left = i + 1
        result = 0
        for i in range(len(customers)):
            result += (
                customers[i]
                if grumpy[i] == 0 or result_left <= i < result_left + minutes
                else 0
            )
        return result


# @lc code=end
