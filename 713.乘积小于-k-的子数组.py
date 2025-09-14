#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        length = len(nums)
        ans = (length + 1) * length // 2
        left = 0
        current = 1
        for right, num in enumerate(nums):
            current *= num
            while current >= k:
                current /= nums[left]
                left += 1
                ans -= length - right
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numSubarrayProductLessThanK(
        [5, 4, 3, 2, 1],
        10,
    )
    print(ans)
