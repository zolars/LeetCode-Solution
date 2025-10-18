#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        ans = mx = 0
        for idx, value in enumerate(values):
            ans = max(ans, mx + value - idx)
            if value + idx > mx:
                mx = value + idx

        return ans


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxScoreSightseeingPair([8, 1, 5, 2, 6])
    print(ans)
