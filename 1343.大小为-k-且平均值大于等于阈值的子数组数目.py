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
        result = 0

        for num in arr[:k]:
            current += num
        result = result + 1 if current >= threshold else result

        left = 0
        for num in arr[k:]:
            current = current + num - arr[left]
            result = result + 1 if current >= threshold else result
            left += 1

        return result


# @lc code=end
