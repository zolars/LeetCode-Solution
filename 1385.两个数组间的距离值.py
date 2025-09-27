#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    def findTheDistanceValue(
        self,
        arr1: list[int],
        arr2: list[int],
        d: int,
    ) -> int:
        ans = 0
        arr1.sort()
        arr2.sort()
        i, j = 0, 0
        while i < len(arr1) or j < len(arr2):
            pass
        return ans


# @lc code=end
