#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    # def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
    #     ans = 0
    #     stock: dict[int, dict[int, int]] = {}
    #     for domino in dominoes:
    #         min_domino = min(domino)
    #         max_domino = max(domino)
    #         if min_domino in stock:
    #             if max_domino in stock[min_domino]:
    #                 ans += stock[min_domino][max_domino]
    #                 stock[min_domino][max_domino] += 1
    #             else:
    #                 stock[min_domino][max_domino] = 1
    #         else:
    #             stock[min_domino] = {max_domino: 1}
    #     return ans

    # 位运算优化：* 16 → << 4
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        d, ans = {}, 0
        for i, j in dominoes:
            c = i * 16 + j if i < j else j * 16 + i
            d[c] = d.get(c, 0) + 1
            ans += d[c] - 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numEquivDominoPairs(
        dominoes=[
            [2, 1],
            [5, 4],
            [3, 7],
            [6, 2],
            [4, 4],
            [1, 8],
            [9, 6],
            [5, 3],
            [7, 4],
            [1, 9],
            [1, 1],
            [6, 6],
            [9, 6],
            [1, 3],
            [9, 7],
            [4, 7],
            [5, 1],
            [6, 5],
            [1, 6],
            [6, 1],
            [1, 8],
            [7, 2],
            [2, 4],
            [1, 6],
            [3, 1],
            [3, 9],
            [3, 7],
            [9, 1],
            [1, 9],
            [8, 9],
        ]
    )
    print(ans)
