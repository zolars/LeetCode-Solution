#
# @lc app=leetcode.cn id=2831 lang=python3
#
# [2831] 找出最长等值子数组
#

# @lc code=start
class Solution:
    # 分组 + 滑动窗口
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        ans = 0
        stock = {}
        for i, num in enumerate(nums):
            if num in stock:
                stock[num].append(i)
            else:
                stock[num] = [i]
        for value in stock.values():
            # 剪枝
            if len(value) <= ans:
                continue
            left = 0
            i = value[left]
            for right, j in enumerate(value):
                while (j - i + 1) - (right - left + 1) > k:
                    left += 1
                    i = value[left]
                ans = max(ans, (right - left + 1))
                # 剪枝
                if len(value) - left + 1 <= ans:
                    break
        return ans

        # @lc code=end
