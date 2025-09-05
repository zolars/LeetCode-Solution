#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        result = 0
        current = 0
        left = 0
        stock = set()
        for right, num in enumerate(nums):
            while num in stock:
                stock.remove(nums[left])
                current -= nums[left]
                left += 1
            stock.add(num)
            current += num
            result = max(result, current)
        return result


# @lc code=end
