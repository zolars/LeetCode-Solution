# Maximal Rectangle


class Solution(object):
    def find(self, (x1, y1), (x2, y2)):
        ans, ans_x, ans_y, x, y = 0, 0, 0, True, True

        for i in xrange(y1, y2 + 1):
            if self.matrix[x2 + 1][i] == "0":
                x = False
                break

        for i in xrange(x1, x2 + 1):
            if self.matrix[i][y2 + 1] == "0":
                y = False
                break

        if x:
            ans_x = self.find((x1, y1), (x2 + 1, y2))
        if y:
            ans_y = self.find((x1, y1), (x2, y2 + 1))
        if (not x) and (not y):
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        ans = max(ans_x, ans_y)
        return ans

    def maximalRectangle1(self, matrix):
        """
        :type self.matrix: List[List[str]]
        :rtype: int
        """
        self.matrix = matrix

        if self.matrix == []:
            return 0

        for i in xrange(len(self.matrix)):
            self.matrix[i] += '0'
        self.matrix.append('0' * len(self.matrix[0]))

        for i in matrix:
            print i

        ans = 0
        for i in xrange(len(self.matrix) - 1):
            for j in xrange(len(self.matrix[0]) - 1):
                if self.matrix[i][j] == '1':
                    ans = max(ans, self.find((i, j), (i, j)))

        return ans

    def maximalRectangle2(self, matrix):
        """
        :type self.matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0

        m, n = len(matrix), len(matrix[0])

        l = [0 for _ in xrange(n)]
        r = [n for _ in xrange(n)]
        h = [0 for _ in xrange(n)]

        ans = 0

        for i in xrange(m):

            left = 0
            for j in xrange(n):
                if matrix[i][j] == "1":
                    l[j] = max(l[j], left)
                    h[j] += 1
                else:
                    l[j] = 0
                    h[j] = 0
                    left = j + 1

            right = n
            for j in reversed(xrange(n)):
                if matrix[i][j] == "1":
                    r[j] = min(right, r[j])
                    ans = max(ans, h[j] * (r[j] - l[j]))
                else:
                    r[j] = n
                    right = j

            print matrix[i]
            print l, r, h, "\n"

        return ans


if __name__ == '__main__':
    matrix = ["01101",
              "11010",
              "01110",
              "11110",
              "11111",
              "00000"]
    print Solution().maximalRectangle2(matrix)
