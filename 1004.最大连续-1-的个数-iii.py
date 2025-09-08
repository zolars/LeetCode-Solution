#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = 0
        len_change = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                len_change += 1
                while len_change > k:
                    len_change -= 1 if nums[left] == 0 else 0
                    left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
