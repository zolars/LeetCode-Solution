#
# @lc app=leetcode.cn id=2900 lang=python3
#
# [2900] 最长相邻不相等子序列 I
#

# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: list[str], groups: List[int]) -> List[str]:
        ans = []
        n = len(groups)
        i = 0
        while i < n:
            ans.append(words[i])
            i += 1
            while i < n and groups[i] == groups[i - 1]:
                i += 1
        return ans


# @lc code=end
