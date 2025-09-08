#
# @lc app=leetcode.cn id=2779 lang=python3
#
# [2779] 数组的最大美丽值
#

# @lc code=start
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        current = nums[0]
        left = 0
        for right, num in enumerate(nums):
            while num > current + k:
                current = num - k
                while nums[left] < current - k:
                    left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
