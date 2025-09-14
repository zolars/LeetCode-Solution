#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#

# @lc code=start
class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        ans = 0
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            current = nums[i] + nums[j]
            if current < target:
                ans += j - i
                i += 1
            else:
                j -= 1
        return ans


# @lc code=end
