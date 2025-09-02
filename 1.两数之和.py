#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

from typing import List


# @lc code=start
class Solution:
    # Bruce Solution
    # 这也太笨了
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, num1 in enumerate(nums):
    #         for j, num2 in enumerate(nums[i + 1 :]):
    #             if num1 + num2 == target:
    #                 return [i, i + 1 + j]
    #     raise SystemExit

    # Hash Table
    # 边构造数据结构边进行数据查找，查找相关的题目都可以用类似的思路
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [i, hashmap[target - num]]
            else:
                hashmap[num] = i

        raise SystemExit


# @lc code=end
