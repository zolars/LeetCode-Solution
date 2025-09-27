#
# @lc app=leetcode.cn id=3467 lang=python3
#
# [3467] 将数组按照奇偶性转化
#

# @lc code=start
class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        cnt1 = sum(x % 2 for x in nums)
        cnt0 = len(nums) - cnt1
        return [0] * cnt0 + [1] * cnt1


# @lc code=end
