#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    # 定长滑动窗口法
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = 0
        current_sum = 0
        for num in nums[:k]:
            current_sum += num
        max_sum = current_sum
        left = 0
        for num in nums[k:]:
            current_sum = current_sum + num - nums[left]
            max_sum = current_sum if current_sum > max_sum else max_sum
            left += 1
        return max_sum / k


# @lc code=end
