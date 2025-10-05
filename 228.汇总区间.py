#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            if i - start == 1:
                ans.append(f"{nums[i - 1]}")
            else:
                ans.append(f"{nums[start]}->{nums[i - 1]}")
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.summaryRanges([0, 1, 2, 4, 5, 7])
    print(ans)
