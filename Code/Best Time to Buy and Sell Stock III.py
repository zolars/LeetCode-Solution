# Best Time to Buy and Sell Stock III


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit_left, profit_all = 0, 0
        begin_1, begin_2 = float("-inf"), float("-inf")
        for i in prices:
            profit_all = min(profit_all, i - begin_2)
            begin_2 = max(begin_2, profit_left + i)

            begin_1 = min(begin_1, i)
            profit_all = max(profit_1, i - begin_1)

        print profit_1


if __name__ == '__main__':
    print Solution().maxProfit([1, 7, 2, 9, 6, 3, 10, 4, 11])
