#
# @lc app=leetcode.cn id=2260 lang=python3
#
# [2260] 必须拿起的最小连续卡牌数
#
from collections import defaultdict


# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        ans = 10**5 + 1
        stock = defaultdict(int)
        for idx, card in enumerate(cards):
            if card in stock:
                ans = min(ans, idx - stock[card] + 1)
                if ans == 2:
                    return 2
            stock[card] = idx
        return ans if ans != 10**5 + 1 else -1


# @lc code=end
