#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        amounts = {key: 0 for key in ["Q", "W", "E", "R"]}
        for c in s:
            amounts[c] += 1
        amounts = {key: max(0, amounts[key] - n // 4) for key in ["Q", "W", "E", "R"]}
        if amounts["Q"] == amounts["W"] == amounts["E"] == amounts["R"] == 0:
            return 0
        ans = len(s)
        left = 0
        current = {key: 0 for key in ["Q", "W", "E", "R"]}
        for right, c in enumerate(s):
            current[c] += 1
            while (
                current["Q"] >= amounts["Q"]
                and current["W"] >= amounts["W"]
                and current["E"] >= amounts["E"]
                and current["R"] >= amounts["R"]
            ):
                ans = min(ans, right - left + 1)
                current[s[left]] -= 1
                left += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.balancedString("WWWWQQQQWQQQ")
    print(ans)
