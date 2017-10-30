# Best Time to Buy and Sell Stock


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_in = 2 ** 32
        profit = 0
        for i in prices:
            if i < price_in:
                price_in = i
                continue
            else:
                profit = max(profit, i - price_in)

        return profit


if __name__ == '__main__':
    print Solution().maxProfit([1, 2, 3, 4])
