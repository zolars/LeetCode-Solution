#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        stock = {}
        for i, num in enumerate(nums):
            if target - num in stock:
                return [i, stock[target - num]]
            else:
                stock[num] = i
        raise SystemError


# @lc code=end
