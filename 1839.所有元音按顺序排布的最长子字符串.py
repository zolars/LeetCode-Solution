#
# @lc app=leetcode.cn id=1839 lang=python3
#
# [1839] 所有元音按顺序排布的最长子字符串
#

# @lc code=start
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = i = 0
        n = len(word)
        while i < n:
            start = i
            i += 1
            aeiou = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
            stock = word[start]
            if stock != "a":
                continue
            while i < n and (
                aeiou[word[i]] == aeiou[stock] or aeiou[word[i]] == aeiou[stock] + 1
            ):
                stock = word[i]
                i += 1
            if stock == "u":
                ans = max(ans, i - start)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.longestBeautifulSubstring(
        "eauoiouieaaoueiuaieoeauoiaueoiaeoiuieuaoiaeouiaueo"
    )
    print(ans)
