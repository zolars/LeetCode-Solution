#
# @lc app=leetcode.cn id=2038 lang=python3
#
# [2038] 如果相邻两个颜色均相同则删除当前颜色
#

# @lc code=start
class Solution:
    # 原始解法（正确但稍慢）：O(n) 时间
    # def winnerOfGame(self, colors: str) -> bool:
    #     n = len(colors)
    #     count_a = count_b = 0
    #     i = 0
    #     while i < n - 1:
    #         start = i
    #         i += 1
    #         while i < n - 1 and colors[i - 1] == colors[i] == colors[i + 1]:
    #             i += 1
    #         if colors[start] == "A":
    #             count_a += i - start - 1
    #         else:
    #             count_b += i - start - 1
    #     return count_a > count_b

    # 优化解法：O(n) 时间，单次遍历，逻辑更简洁清晰
    def winnerOfGame(self, colors: str) -> bool:
        count_a = count_b = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    count_a += 1
                else:
                    count_b += 1
        return count_a > count_b


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.winnerOfGame("AAAABBBB")
    print(ans)
