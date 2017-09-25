class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        res = [0 for i in xrange(n)]
        res[0], res[1] = 1, 2

        for i in xrange(2, n):
            res[i] = res[i - 1] + res[i - 2]

        return res[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(200))
