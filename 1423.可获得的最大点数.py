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
    #     result = current
    #     for right in range(k):
    #         current = (
    #             current
    #             + cardPoints[len(cardPoints) - right - 1]
    #             - cardPoints[k - right - 1]
    #         )
    #         result = max(current, result)
    #     return result

    # 从中间找最小
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        real_k = len(cardPoints) - k
        current = 0
        for card in cardPoints[:real_k]:
            current += card
        result = current
        for left, card in enumerate(cardPoints[real_k:]):
            current = current + card - cardPoints[left]
            result = min(current, result)
        return sum(cardPoints) - result


# @lc code=end
