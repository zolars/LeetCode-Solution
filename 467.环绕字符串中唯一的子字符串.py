#
# @lc app=leetcode.cn id=467 lang=python3
#
# [467] 环绕字符串中唯一的子字符串
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        i = 0
        n = len(s)
        stock = {c: 1 for c in s}
        while i < n:
            start = i
            i += 1
            while i < n and (
                (ord(s[i]) == ord(s[i - 1]) + 1) or (s[i - 1] == "z" and s[i] == "a")
            ):
                stock[s[i]] = max(stock[s[i]], i - start + 1)
                i += 1
        return sum(stock.values())


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findSubstringInWraproundString("zab")
    print(ans)
