#
# @lc app=leetcode.cn id=3132 lang=python3
#
# [3132] 找出与数组相加的整数 II
#

# @lc code=start
class Solution:
    def minimumAddedInteger(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> int:
        ans = 1001
        nums1.sort()
        nums2.sort()
        m, n = len(nums1), len(nums2)
        for i, num1 in enumerate(nums1[0 : m - n + 1]):
            current = nums2[0] - num1
            flag = True
            chance = 2
            j = 0
            while i + j < m and j < n:
                if nums1[i + j] + current != nums2[j]:
                    if (
                        chance > 0
                        and i + j + 1 < m
                        and nums1[i + j + 1] + current == nums2[j]
                    ):
                        i += 1
                        chance -= 1
                    elif (
                        chance > 1
                        and i + j + 2 < m
                        and nums1[i + j + 2] + current == nums2[j]
                    ):
                        i += 2
                        chance -= 1
                    else:
                        flag = False
                        break
                j += 1
            if flag and j == n:
                ans = min(ans, current)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.minimumAddedInteger(
        [2, 6, 7, 7, 8],
        [5, 6, 7],
    )
    print(ans)
