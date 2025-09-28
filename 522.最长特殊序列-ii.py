#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#

# @lc code=start
class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def is_subseq(s: str, t: str) -> bool:
            i = 0
            for c in t:
                if s[i] == c:
                    i += 1
                    if i == len(s):  # 所有字符匹配完毕
                        return True  # s 是 t 的子序列
            return False

        ans = -1
        for i, s in enumerate(strs):
            if len(s) > ans:
                flag = True
                for j, t in enumerate(strs):
                    if i != j and is_subseq(s, t):
                        flag = False
                ans = len(s) if flag else ans
        return ans


# @lc code=end
