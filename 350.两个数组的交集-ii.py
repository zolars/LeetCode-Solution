#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> list[int]:
        nums1.sort()
        nums2.sort()
        m, n = len(nums1), len(nums2)
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return nums1[0:k]


# @lc code=end
