#
# @lc app=leetcode.cn id=1855 lang=python3
#
# [1855] 下标对中的最大距离
#

# @lc code=start
class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        ans = 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if i <= j and nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            elif i < j:
                i += 1
            elif i == j:
                i += 1
                j += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxDistance(
        [55, 30, 5, 4, 2],
        [100, 20, 10, 10, 5],
    )
    print(ans)
