#
# @lc app=leetcode.cn id=3350 lang=python3
#
# [3350] 检测相邻递增子数组 II
#

# @lc code=start
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        ans = i = 0
        n = len(nums)
        stock = 0
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            ans = max(ans, min(i - start, stock), (i - start) // 2)
            stock = i - start
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxIncreasingSubarrays(
        # nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1],
        nums=[1, 2, -2, -1, 18],
    )
    print(ans)
