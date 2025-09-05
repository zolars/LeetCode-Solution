#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    # 不定长滑窗
    def minOperations(self, nums: list[int], x: int) -> int:
        sums = sum(nums)
        if sums == x:
            return len(nums)
        if sums < x:
            return -1
        result = 0
        current = 0
        left = 0
        for right, num in enumerate(nums):
            current += num
            while current > sums - x:
                current -= nums[left]
                left += 1
            if current == sums - x:
                result = max(result, right - left + 1)
        return len(nums) - result if result > 0 else -1


# @lc code=end
