# House Robber II


class Solution(object):
    def rob(self, nums):
        """
        :type nums_1: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums_1 = nums[1:]
        dp = [0, 0]
        for i in xrange(len(nums_1)):
            add = max(dp[i] + nums_1[i], dp[i + 1])
            dp.append(add)
        ans = dp[-1]

        nums_2 = nums[:-1]
        dp = [0, 0]
        for i in xrange(len(nums_2)):
            add = max(dp[i] + nums_2[i], dp[i + 1])
            dp.append(add)
        ans = max(ans, dp[-1])

        return ans


if __name__ == '__main__':
    print Solution().rob([1])
