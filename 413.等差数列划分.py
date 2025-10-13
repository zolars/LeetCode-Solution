#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    # TODO: 边界条件玩花的
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = i = 0
        n = len(nums)
        while i <= n - 3:
            start = i
            if nums[start + 1] - nums[start] != nums[start + 2] - nums[start + 1]:
                i += 1
                continue
            delta = nums[start + 1] - nums[start]
            i += 2
            while i < n and nums[i] - nums[i - 1] == delta:
                i += 1
            ans += (i - start - 2) * (i - start - 1) // 2
            i -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numberOfArithmeticSlices([1, 2, 3, 4])
    print(ans)
