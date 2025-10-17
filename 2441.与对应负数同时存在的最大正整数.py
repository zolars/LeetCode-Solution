#
# @lc app=leetcode.cn id=2441 lang=python3
#
# [2441] 与对应负数同时存在的最大正整数
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ans = -1
        stock = set()
        for num in nums:
            if -num in stock:
                ans = max(ans, abs(num))
            else:
                stock.add(num)
        return ans


# @lc code=end
