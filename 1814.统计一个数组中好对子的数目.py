#
# @lc app=leetcode.cn id=1814 lang=python3
#
# [1814] 统计一个数组中好对子的数目
#


# @lc code=start
class Solution:
    # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    def countNicePairs(self, nums: list[int]) -> int:
        stock = {}
        ans = 0
        for num in nums:
            # calculate num - rev(num)
            value = int(str(num)[::-1]) - num
            if value in stock:
                ans += stock[value]
            else:
                stock[value] = 0
            stock[value] += 1
        return ans % (10**9 + 7)


# @lc code=end
