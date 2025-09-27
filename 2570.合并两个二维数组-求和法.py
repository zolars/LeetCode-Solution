#
# @lc app=leetcode.cn id=2570 lang=python3
#
# [2570] 合并两个二维数组 - 求和法
#

# @lc code=start
class Solution:
    def mergeArrays(
        self,
        nums1: list[list[int]],
        nums2: list[list[int]],
    ) -> list[list[int]]:
        ans = []
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m or j < n:
            if i == m:
                ans.append(nums2[j])
                j += 1
            elif j == n:
                ans.append(nums1[i])
                i += 1
            elif nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        return ans


# @lc code=end
