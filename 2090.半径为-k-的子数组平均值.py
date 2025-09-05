#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#

# @lc code=start
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if len(nums) < 2 * k + 1:
            return [-1] * len(nums)
        current = 0
        for num in nums[: k * 2 + 1]:
            current += num
        avgs = [-1] * k + [current // (k * 2 + 1)]
        right = k * 2 + 1
        for num in nums[k * 2 + 1 :]:
            current = current + num - nums[right - k * 2 - 1]
            avgs.append(current // (k * 2 + 1))
            right += 1
        avgs += [-1] * k
        return avgs


# @lc code=end
