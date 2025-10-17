#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#

# @lc code=start
class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ans = 0
        min_num = 10**9 + 1
        for num in nums:
            min_num = min(min_num, num)
            ans = max(ans, num - min_num)
        return ans if ans > 0 else -1


# @lc code=end
