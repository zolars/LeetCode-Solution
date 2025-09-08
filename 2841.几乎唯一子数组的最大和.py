#
# @lc app=leetcode.cn id=2841 lang=python3
#
# [2841] 几乎唯一子数组的最大和
#

# @lc code=start
class Solution:
    # 看似会快的二重循环
    # def maxSum(self, nums: list[int], m: int, k: int) -> int:
    #     stock = set()
    #     current_sum = 0
    #     for num in nums[:k]:
    #         stock.add(num)
    #         current_sum += num
    #     ans = current_sum if len(stock) >= m else 0
    #     for left, num in enumerate(nums[k:]):
    #         if num != nums[left]:
    #             current_sum = current_sum + num - nums[left]
    #             stock.add(num)
    #             remove_flag = True
    #             for num2 in nums[left + 1 : left + k + 1]:
    #                 if num2 == nums[left]:
    #                     remove_flag = False
    #                     break
    #             if remove_flag:
    #                 stock.remove(nums[left])
    #             ans = (
    #                 current_sum if len(stock) >= m and current_sum > ans else ans
    #             )
    #     return ans

    # 看似会快的list2set, 和上面方法本质一样
    # def maxSum(self, nums: list[int], m: int, k: int) -> int:
    #     subset = set(nums[:k])
    #     current_sum = sum(nums[:k])
    #     ans = current_sum if len(subset) >= m else 0
    #     for left, num in enumerate(nums[k:]):
    #         current_sum = current_sum + num - nums[left]
    #         subset = set(nums[left + 1 : left + k + 1])
    #         ans = (
    #             current_sum if len(subset) >= m and current_sum > ans else ans
    #         )
    #     return ans

    # 看似会快的二重循环改哈希表
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        stock = {}
        current_sum = 0
        for num in nums[:k]:
            if num in stock:
                stock[num] += 1
            else:
                stock[num] = 1
            current_sum += num
        ans = current_sum if len(stock) >= m else 0
        for left, num in enumerate(nums[k:]):
            if num != nums[left]:
                current_sum = current_sum + num - nums[left]
                if num in stock:
                    stock[num] += 1
                else:
                    stock[num] = 1
                stock[nums[left]] -= 1
                if stock[nums[left]] == 0:
                    stock.pop(nums[left])
                ans = current_sum if len(stock) >= m and current_sum > ans else ans
        return ans


# @lc code=end
