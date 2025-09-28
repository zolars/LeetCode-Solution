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
        # print(arr1)
        # print(arr2)
        i, j = 0, 0
        while i < len(arr1):
            if j == len(arr2):
                ans += 1
                i += 1
            elif arr2[j] < arr1[i] and arr1[i] - arr2[j] > d:
                j += 1
            elif arr2[j] > arr1[i] and arr2[j] - arr1[i] > d:
                i += 1
                ans += 1
            elif abs(arr2[j] - arr1[i]) <= d:
                i += 1

        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findTheDistanceValue(
        [-3, 10, 2, 8, 0, 10],
        [-9, -1, -4, -9, -8],
        9,
    )
    print(ans)
