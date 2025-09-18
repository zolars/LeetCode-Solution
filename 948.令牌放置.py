#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        ans = 0
        current = 0
        n = len(tokens)
        tokens.sort()
        if n == 0 or tokens[0] > power:
            return 0
        i, j = 0, n - 1
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                current += 1
                ans = max(current, ans)
                i += 1
            elif current > 0:
                current -= 1
                power += tokens[j]
                j -= 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.bagOfTokensScore(tokens=[], power=150)
    print(ans)
