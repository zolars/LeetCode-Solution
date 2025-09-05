#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    # 注意到，这是一个首尾相连的顺序列表
    # 肯定要从这个特点出发减少步骤

    # O(n)解
    # def findMin(self, nums: list[int]) -> int:
    #     left_num = -5001
    #     for num in nums:
    #         if num < left_num:
    #             return num
    #         else:
    #             left_num = num
    #     return nums[0]

    # 最傻二分法解
    # def findMin(self, nums: list[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     if len(nums) == 2:
    #         return min(nums[0], nums[1])
    #     if nums[len(nums) // 2 - 1] > nums[len(nums) // 2]:
    #         return nums[len(nums) // 2]
    #     else:
    #         return min(
    #             self.findMin(nums[: len(nums) // 2]),
    #             self.findMin(nums[len(nums) // 2 + 1 :]),
    #         )

    # 二分法：中间哨兵和左右边界：递归
    # def findMin(self, nums: list[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     if nums[len(nums) // 2 - 1] > nums[len(nums) // 2]:
    #         return nums[len(nums) // 2]
    #     elif nums[len(nums) // 2] > nums[-1]:
    #         return self.findMin(nums[len(nums) // 2 :])
    #     else:
    #         return self.findMin(nums[:-1])

    # 二分法：中间哨兵和左右边界：迭代
    # def findMin(self, nums: list[int]) -> int:
    #     left, right = 0, len(nums) - 1
    #     while True:
    #         mid = (left + right) // 2
    #         if left == right:
    #             return nums[left]
    #         elif nums[mid] > nums[mid + 1]:
    #             return nums[mid + 1]
    #         elif nums[mid + 1] > nums[right]:
    #             left = mid + 1
    #         else:
    #             right -= 1

    # 二分法：完美
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            print(left, right, pivot)
            if nums[pivot] < nums[left]:
                right = pivot
            elif nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right -= 1

        return nums[left]


# @lc code=end
