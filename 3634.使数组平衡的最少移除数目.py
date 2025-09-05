#
# @lc app=leetcode.cn id=3634 lang=python3
#
# [3634] 使数组平衡的最少移除数目
#

# @lc code=start
class Solution:
    # 至多是其最小元素的k倍
    # 先排序
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_length = 0
        left = 0
        for right, num in enumerate(nums):
            while num > nums[left] * k:
                left += 1
            max_length = max(max_length, right - left + 1)
        return len(nums) - max_length


# @lc code=end
