#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        result = 0
        len0 = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                len0 += 1
                while len0 > 1:
                    len0 -= 1 if nums[left] == 0 else 0
                    left += 1
            result = max(result, right - left + 1)
        return result - 1


# @lc code=end
