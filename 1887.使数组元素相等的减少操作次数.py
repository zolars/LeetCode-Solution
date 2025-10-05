#
# @lc app=leetcode.cn id=1887 lang=python3
#
# [1887] 使数组元素相等的减少操作次数
#

# @lc code=start
class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        ans = i = 0
        while i < n:
            i += 1
            while i < n and nums[i - 1] == nums[i]:
                i += 1
            if i < n:
                ans += i
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.reductionOperations([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(ans)
