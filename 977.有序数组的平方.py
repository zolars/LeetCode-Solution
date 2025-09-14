#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        i, j, p = 0, n - 1, n - 1
        while i < j:
            if abs(nums[i]) >= abs(nums[j]):
                ans[p] = nums[i] * nums[i]
                i += 1
                p -= 1
            else:
                ans[p] = nums[j] * nums[j]
                j -= 1
                p -= 1
        ans[0] = nums[i] * nums[i]
        return ans


# @lc code=end
