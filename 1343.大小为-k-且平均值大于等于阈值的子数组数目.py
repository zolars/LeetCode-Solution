#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        current = 0
        ans = 0

        for num in arr[:k]:
            current += num
        ans = ans + 1 if current >= threshold else ans

        left = 0
        for num in arr[k:]:
            current = current + num - arr[left]
            ans = ans + 1 if current >= threshold else ans
            left += 1

        return ans


# @lc code=end
