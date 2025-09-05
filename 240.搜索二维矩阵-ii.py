#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    # 每行的元素从左到右升序排列
    # 每列的元素从上到下升序排列

    # 只找对角线的递推解
    # def searchMatrix(self, matrix, target: int) -> bool:
    #     for i in range(min(len(matrix), len(matrix[0]))):
    #         if matrix[i][i] == target:
    #             return True
    #         elif i + 1 == min(len(matrix), len(matrix[0])):
    #             new_matrix = [[]]
    #             if len(matrix) == len(matrix[0]):
    #                 return False
    #             elif len(matrix) < len(matrix[0]):
    #                 new_matrix = [row[len(matrix) :] for row in matrix]
    #             else:
    #                 new_matrix = matrix[len(matrix[0]) :]

    #             return self.searchMatrix(new_matrix, target)
    #         elif matrix[i][i] < target and matrix[i + 1][i + 1] > target:
    #             new_matrix_1 = [row[i + 1 :] for row in matrix][: i + 1]
    #             new_matrix_2 = [row[: i + 1] for row in matrix][i + 1 :]
    #             return self.searchMatrix(new_matrix_1, target) or self.searchMatrix(
    #                 new_matrix_2, target
    #             )

    # 四边查找
    # def searchMatrix(self, matrix, target: int) -> bool:
    #     top, bottom = 0, len(matrix) - 1
    #     left, right = 0, len(matrix[0]) - 1
    #     while top <= bottom and left <= right:
    #         # 处理左上
    #         if matrix[top][left] > target:
    #             return False
    #         # 处理右上
    #         if matrix[top][right] < target:
    #             top += 1
    #             continue
    #         if matrix[top][right] > target:
    #             right -= 1
    #             continue
    #         # 处理左下
    #         if matrix[bottom][left] > target:
    #             bottom -= 1
    #             continue
    #         if matrix[bottom][left] < target:
    #             left += 1
    #             continue
    #         # 处理右下
    #         if matrix[bottom][right] < target:
    #             return False
    #         # 只剩下等于的情况了
    #         return True

    # Z字查找
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False


# @lc code=end
