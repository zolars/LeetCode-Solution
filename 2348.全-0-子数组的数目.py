#
# @lc app=leetcode.cn id=2348 lang=python3
#
# [2348] 全 0 子数组的数目
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = i = 0
        while i < n:
            start = i
            while i < n and nums[i] == 0:
                i += 1
            ans += (i - start + 1) * (i - start) // 2
            i += 1
        return ans


# @lc code=end
