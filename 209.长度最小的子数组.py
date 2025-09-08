#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    # 滑动窗口的答案更新时机也很重要
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = n + 1
        i, stock = 0, 0
        for j, num in enumerate(nums):
            stock += num
            while stock >= target:
                ans = min(ans, j - i + 1)
                stock -= nums[i]
                i += 1
        if ans > n:
            return 0
        else:
            return ans


# @lc code=end
