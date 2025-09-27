#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(
        self,
        nums1: list[int],
        m: int,
        nums2: list[int],
        n: int,
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        m -= 1
        n -= 1
        while k >= 0:
            if m == -1:
                nums1[k] = nums2[n]
                n -= 1
            elif n == -1:
                break
            elif nums1[m] <= nums2[n]:
                nums1[k] = nums2[n]
                n -= 1
            else:
                nums1[k] = nums1[m]
                m -= 1

            k -= 1


# @lc code=end
