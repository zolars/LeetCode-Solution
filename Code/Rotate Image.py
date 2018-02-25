# Rotate Image


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in matrix:
            print i
        print("\n")

        left = 0
        right = len(matrix) - 1
        while right - left > 0:
            for i in xrange(right - left):
                mark = matrix[left][left + i]
                matrix[left][left + i] = matrix[right - i][left]
                matrix[right - i][left] = matrix[right][right - i]
                matrix[right][right - i] = matrix[left + i][right]
                matrix[left + i][right] = mark

            for i in matrix:
                print i
            print("\n")

            left += 1
            right -= 1


if __name__ == "__main__":
    Solution().rotate(
        [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ],
    )
