# Ugly Number II


class Solution(object):
    ans = sorted((2 ** i) * (3 ** j) * (5 ** k)
                 for i in xrange(32)
                 for j in xrange(20)
                 for k in xrange(14))

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ans[n - 1]


if __name__ == '__main__':
    print Solution().nthUglyNumber(331)
