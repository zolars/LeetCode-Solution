#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    # 笨办法
    # def longestConsecutive(self, nums) -> int:
    #     if len(nums) == 0:
    #         return 0

    #     def _quicksort(a, lo, hi):
    #         if lo >= hi:
    #             return
    #         pivot = a[(lo + hi) // 2]
    #         i, j = lo, hi
    #         while i <= j:
    #             while a[i] < pivot:
    #                 i += 1
    #             while a[j] > pivot:
    #                 j -= 1
    #             if i <= j:
    #                 a[i], a[j] = a[j], a[i]
    #                 i += 1
    #                 j -= 1
    #         _quicksort(a, lo, j)
    #         _quicksort(a, i, hi)
    #     _quicksort(nums, 0, len(nums) - 1)
    #     max_length: int = 0
    #     current_length: int = 0
    #     correct_num: int = nums[0]
    #     for num in nums:
    #         if num == correct_num:
    #             current_length += 1
    #             correct_num += 1
    #         elif num == correct_num - 1:
    #             pass
    #         else:
    #             max_length = max(max_length, current_length)
    #             current_length = 1
    #             correct_num = num + 1
    #     max_length = max(max_length, current_length)
    #     return max_length

    # 哈希
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                while current_num + 1 in nums:
                    current_num += 1
                max_length = max(current_num - num + 1, max_length)
        return max_length


# @lc code=end
