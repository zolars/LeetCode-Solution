#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    # # 复习：写个双指针
    # def maxPower(self, s: str) -> int:
    #     ans = 1
    #     i, j = 0, 1
    #     while j < len(s):
    #         if s[i] != s[j]:
    #             ans = max(ans, j - i)
    #             i = j
    #         j += 1
    #     return max(ans, j - i)

    # 复习：写个分组循环
    def maxPower(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[start]:
                i += 1
            ans = max(ans, i - start)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxPower("cc")
    print(ans)
