#
# @lc app=leetcode.cn id=2110 lang=python3
#
# [2110] 股票平滑下跌阶段的数目
#

# @lc code=start
class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        n = len(prices)
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and prices[i] == prices[i - 1] - 1:
                i += 1
            ans += (i - start) * (i - start + 1) // 2
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.getDescentPeriods([8, 6, 7, 7])
    print(ans)
