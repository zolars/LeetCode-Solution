#
# @lc app=leetcode.cn id=2958 lang=python3
#
# [2958] 最多 K 个重复元素的最长子数组
#

# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        result = 0
        left = 0
        stock = {}
        for right, num in enumerate(nums):
            if num in stock:
                stock[num] += 1
            else:
                stock[num] = 1
            while stock[num] > k:
                stock[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


# @lc code=end
