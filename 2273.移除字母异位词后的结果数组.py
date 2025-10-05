#
# @lc app=leetcode.cn id=2273 lang=python3
#
# [2273] 移除字母异位词后的结果数组
#

# @lc code=start
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        n = len(words)
        ans = []
        i = 0
        while i < n:
            start = i
            ans += [words[start]]
            i += 1
            while i < n and sorted(words[i]) == sorted(words[i - 1]):
                i += 1
        return ans


# @lc code=end
