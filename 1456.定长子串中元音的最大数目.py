#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    # 存子字符串
    # def maxVowels(self, s: str, k: int) -> int:
    #     rhythms = {"a", "e", "i", "o", "u"}
    #     substr = []
    #     ans = 0
    #     current = 0
    #     for c in s:
    #         if c in rhythms:
    #             current += 1
    #         substr.append(c)
    #         if len(substr) > k:
    #             if substr.pop(0) in rhythms:
    #                 current -= 1
    #         ans = current if current > ans else ans
    #         if ans == k:
    #             return ans
    #     return ans

    # 不存子字符串，用右指针控制
    def maxVowels(self, s: str, k: int) -> int:
        rhythms = {"a", "e", "i", "o", "u"}
        current = 0
        ans = 0
        right = 0
        for c in s:
            if c in rhythms:
                current += 1
            if right - k >= 0 and s[right - k] in rhythms:
                current -= 1
            ans = current if current > ans else ans
            if ans == k:
                return ans
            right += 1

        return ans


# @lc code=end
