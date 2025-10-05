#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n = len(nums)
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            ans = max(ans, i - start)
        return ans


# @lc code=end
