#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    # TODO: 倒序遍历特判的情况需要深入理解
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i, j = 0, n - 1
        while i < j:
            if arr[i] == 0:
                j -= 1
            i += 1
        left, right = j, n - 1

        # 特判：就是存在一个奇偶的问题对吧
        if i == j and arr[i] == 0:
            arr[right] = 0
            right -= 1
            left -= 1  # 排除这个边界零，避免后续再次复写

        while left >= 0:
            if arr[left] == 0:
                arr[right] = 0
                right -= 1

            arr[right] = arr[left]
            right -= 1
            left -= 1


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    sol.duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7])
