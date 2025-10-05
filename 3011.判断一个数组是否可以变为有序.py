#
# @lc app=leetcode.cn id=3011 lang=python3
#
# [3011] 判断一个数组是否可以变为有序
#

# @lc code=start
class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            start = i
            ones = nums[start].bit_count()
            i += 1
            while i < n and nums[i].bit_count() == ones:
                i += 1
            nums[start:i] = sorted(nums[start:i])
        return nums == sorted(nums)


# @lc code=end
