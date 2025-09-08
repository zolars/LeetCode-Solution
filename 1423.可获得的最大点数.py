#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    # 从左右找最大
    # def maxScore(self, cardPoints: list[int], k: int) -> int:
    #     current = 0
    #     for left in range(k):
    #         current += cardPoints[left]
    #     ans = current
    #     for right in range(k):
    #         current = (
    #             current
    #             + cardPoints[len(cardPoints) - right - 1]
    #             - cardPoints[k - right - 1]
    #         )
    #         ans = max(current, ans)
    #     return ans

    # 从中间找最小
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        real_k = len(cardPoints) - k
        current = 0
        for card in cardPoints[:real_k]:
            current += card
        ans = current
        for left, card in enumerate(cardPoints[real_k:]):
            current = current + card - cardPoints[left]
            ans = min(current, ans)
        return sum(cardPoints) - ans


# @lc code=end
