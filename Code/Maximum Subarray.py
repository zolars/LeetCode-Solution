class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for i in range(len(nums))[1:]:
            nums[i] = max(nums[i] + nums[i - 1], nums[i])
            ans = max(ans, nums[i])

        return ans


if __name__ == '__main__':
    print(Solution().maxSubArray([1, -2]))
