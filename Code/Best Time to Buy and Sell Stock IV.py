# Best Time to Buy and Sell Stock IV


class Solution:
    def maxProfit(self, k, prices):
        if k >= len(prices) / 2:
            return self.maxAtMostNPairsProfit(prices)

        return self.maxAtMostKPairsProfit(prices, k)

    def maxAtMostNPairsProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        print max_buy
        print max_sell

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i / 2 + 1) + 1):
                print "===", i, j, "==="

                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
                print
                print max_buy
                print max_sell
                print

        return max_sell[-1]


if __name__ == "__main__":
    print Solution().maxAtMostKPairsProfit([3, 7, 2, 8, 6, 4, 9], 2)
    # 3, 7, 2, 8, 6, 3, 9, 4, 11
