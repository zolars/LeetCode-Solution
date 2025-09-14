#
# @lc app=leetcode.cn id=3643 lang=python3
#
# [3643] 垂直翻转子矩阵
#

# @lc code=start
class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        i, j = x, x + k - 1
        while i < j:
            (
                grid[i][y : y + k],
                grid[j][y : y + k],
            ) = (
                grid[j][y : y + k],
                grid[i][y : y + k],
            )
            i += 1
            j -= 1
        return grid


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.reverseSubmatrix(
        grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        x=1,
        y=0,
        k=3,
    )
    print(ans)
