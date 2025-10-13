#
# @lc app=leetcode.cn id=3105 lang=python3
#
# [3105] 最长的严格递增或递减子数组
#

# @lc code=start
class Solution:
    # O(2n)
    # def longestMonotonicSubarray(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     ans1 = i = 0
    #     while i < n:
    #         start = i
    #         i += 1
    #         while i < n and nums[i] > nums[i - 1]:
    #             i += 1
    #         ans1 = max(ans1, i - start)
    #     ans2 = i = 0
    #     while i < n:
    #         start = i
    #         i += 1
    #         while i < n and nums[i] < nums[i - 1]:
    #             i += 1
    #         ans2 = max(ans2, i - start)
    #     return max(ans1, ans2)

    # TODO: O(n) 时间复杂度:遍历数组一次
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        # 最长单调子数组的长度,至少为1(单个元素也算)
        ans = 1
        # 当前遍历位置
        i = 0
        # 数组长度
        n = len(nums)
        # 遍历数组,直到倒数第二个元素
        while i < n - 1:
            # 如果当前元素和下一个元素相等,不满足严格单调
            if nums[i + 1] == nums[i]:
                i += 1  # 跳过当前位置,继续寻找
                continue
            # 记录当前单调子数组的起始位置
            start = i
            # 确定单调性:True表示严格递增,False表示严格递减
            is_increasing = nums[i + 1] > nums[i]
            # i和i+1已经满足单调性,从i+2开始继续判断
            i += 2
            # 继续向后扩展,只要满足:
            # 1. 没有越界
            # 2. 当前元素与前一个元素不相等(严格单调)
            # 3. 当前元素与前一个元素的大小关系与之前确定的单调性一致
            while (
                i < n
                and nums[i] != nums[i - 1]
                and (nums[i] > nums[i - 1]) == is_increasing
            ):
                i += 1
            # 此时从start到i-1构成一个最长的单调子数组
            # 更新最大长度
            ans = max(ans, i - start)
            # 回退一步,因为i位置可能是下一个单调子数组的起点
            i -= 1
        return ans


# @lc code=end
