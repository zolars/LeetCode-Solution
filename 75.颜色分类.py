#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stock = {0: 0, 1: 0, 2: 0}
        for num in nums:
            stock[num] += 1

        for i in range(stock[0]):
            nums[i] = 0
        for i in range(stock[1]):
            nums[i + stock[0]] = 1
        for i in range(stock[2]):
            nums[i + stock[0] + stock[1]] = 2


# @lc code=end
