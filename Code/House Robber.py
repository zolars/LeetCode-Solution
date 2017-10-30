# House Robber


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0, 0]
        for i in xrange(len(nums)):
            add = max(dp[i] + nums[i], dp[i + 1])
            dp.append(add)
        return dp[-1]


if __name__ == '__main__':
    print Solution().rob([3, 4, 5, 8, 3, 10])
