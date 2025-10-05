#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

# @lc code=start
class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        ans = i = 0
        while i < n - 1:
            # 先寻找上升段的起点
            while i < n - 1 and arr[i] >= arr[i + 1]:
                i += 1
            start = i
            while i < n - 1 and arr[i] < arr[i + 1]:
                i += 1
            if i == n - 1 or i == start or arr[i] == arr[i + 1]:
                continue
            while i < n - 1 and arr[i] > arr[i + 1]:
                i += 1
            ans = max(ans, i - start + 1)

        return ans


# @lc code=end
