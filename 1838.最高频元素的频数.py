#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        current = 0
        left = 0
        for right, num in enumerate(nums):
            current += (num - nums[right - 1]) * (right - left)
            while current > k:
                current -= num - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
