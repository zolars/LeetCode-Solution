#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def findLongestWord(
        self,
        s: str,
        dictionary: list[str],
    ) -> str:
        ans = ""
        max_len = 0
        for t in dictionary:
            if len(t) > max_len or (len(t) == max_len and t < ans):
                m, n = len(s) - 1, len(t) - 1
                while m >= 0 and n >= 0:
                    if s[m] == t[n]:
                        m -= 1
                        n -= 1
                    else:
                        m -= 1
                if n == -1:
                    ans = t
                    max_len = len(ans)
        return ans


# @lc code=end
