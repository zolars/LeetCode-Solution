# Best Time to Buy and Sell Stock IV


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices):
            buy, ans = 2 ** 32, 0
            for i in prices:
                if i < buy:
                    buy = i
                else:
                    ans += i - buy
                    buy = i
            return ans

        buy = [-2 ** 32 for _ in xrange(k + 1)]
        sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, i + 2 if i < k else k + 1):
                buy[j] = max(buy[j], sell[j - 1] - prices[i])
                sell[j] = max(sell[j],  buy[j] + prices[i])

        return sell[-1]


if __name__ == '__main__':
    print Solution().maxProfit(100, [3, 7, 2, 5, 6, 8])
