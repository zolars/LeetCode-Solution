#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans, min_price = 0, 10001
        for price in prices:
            min_price = min(min_price, price)
            ans = max(ans, price - min_price)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxProfit(prices=[7, 6, 4, 3, 1])
    print(ans)
