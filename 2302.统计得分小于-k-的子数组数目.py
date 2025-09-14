#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        length = len(nums)
        ans = length * (length + 1) // 2
        left = 0
        current_sum = 0
        current_len = 0
        for right, num in enumerate(nums):
            current_sum += num
            current_len += 1
            while current_sum * current_len >= k:
                ans -= length - right
                current_sum -= nums[left]
                current_len -= 1
                left += 1
        return ans


# @lc code=end
