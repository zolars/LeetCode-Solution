# Triangle


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == [[]]:
            return 0

        dp = [triangle[0][0]] + [0 for _ in xrange(len(triangle) - 1)]

        for i in triangle[1:]:
            right = dp[0]
            dp[0] = dp[0] + i[0]
            for j in xrange(1, len(i) - 1):
                left = dp[j]
                dp[j] = min(dp[j], right) + i[j]
                right = left

            dp[len(i) - 1] = i[len(i) - 1] + right

        print dp

        ans = 1000000
        for i in dp:
            ans = min(i, ans)
        return ans


if __name__ == '__main__':
    print Solution().minimumTotal(
        [
            []
        ])
