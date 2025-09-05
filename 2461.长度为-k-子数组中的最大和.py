#
# @lc app=leetcode.cn id=2461 lang=python3
#
# [2461] 长度为 K 子数组中的最大和
#

# @lc code=start
class Solution:
    # 普通的滑动窗口，easy
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        current = 0
        stock = {}
        for num in nums[:k]:
            if num in stock:
                stock[num] += 1
            else:
                stock[num] = 1
            current += num
        result = current if len(stock) == k else result
        for left, num in enumerate(nums[k:]):
            current = current + num - nums[left]
            if nums[left] != num:
                if num in stock:
                    stock[num] += 1
                else:
                    stock[num] = 1
                stock[nums[left]] -= 1
                if stock[nums[left]] == 0:
                    stock.pop(nums[left])
                result = current if len(stock) == k and current > result else result
        return result


# @lc code=end
