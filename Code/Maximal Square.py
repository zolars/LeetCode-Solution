# Maximal Square


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        l = [0 for _ in xrange(n)]
        r = [n for _ in xrange(n)]
        h = [0 for _ in xrange(n)]

        ans = 0
        for i in xrange(m):
            left = 0
            for j in xrange(n):
                if matrix[i][j] == "1":
                    l[j] = max(l[j], left)
                else:
                    l[j] = 0
                    left = j + 1

            right = n
            for j in reversed(xrange(n)):
                if matrix[i][j] == "1":
                    r[j] = min(r[j], right)
                else:
                    r[j] = n
                    right = j

            for j in reversed(xrange(n)):
                if matrix[i][j] == "1":
                    h[j] += 1
                    ans = max(ans, min((r[j] - l[j]), h[j]) ** 2)
                else:
                    h[j] = 0
            print l, r, h

        return ans


if __name__ == '__main__':
    matrix = ["10100",
              "10111",
              "11111",
              "10010"]
    print(Solution().maximalSquare(matrix))
