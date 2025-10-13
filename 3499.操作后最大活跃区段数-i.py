#
# @lc app=leetcode.cn id=3499 lang=python3
#
# [3499] 操作后最大活跃区段数 I
#

# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        stock = []
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            start = i
            i += 1
            while i < n and s[i - 1] == s[i]:
                i += 1
            if s[start] == "1":
                ans += i - start
            stock.append(i - start)
        l, r = 100001, 100001
        if s[0] == "0" and len(stock) > 2:
            l, r = 0, 2
        elif s[0] == "1" and len(stock) > 3:
            l, r = 1, 3
        delta = 0
        while r < len(stock):
            delta = max(delta, stock[l] + stock[r])
            l += 2
            r += 2
        return ans + delta


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxActiveSectionsAfterTrade("1000100")
    print(ans)
