#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#

# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        ans = i = 0
        n = len(colors)
        while i < n:
            start = i
            color = colors[start]
            max_value = 0
            while i < n and colors[i] == color:
                max_value = max(max_value, neededTime[i])
                i += 1
            ans += max_value
        return sum(neededTime) - ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.minCost("abaac", [1, 2, 3, 4, 5])
    print(ans)
