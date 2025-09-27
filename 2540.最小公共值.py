#
# @lc app=leetcode.cn id=2540 lang=python3
#
# [2540] 最小公共值
#

# @lc code=start
class Solution:
    def getCommon(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> int:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1


# @lc code=end
