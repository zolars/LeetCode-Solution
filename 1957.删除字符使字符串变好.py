#
# @lc app=leetcode.cn id=1957 lang=python3
#
# [1957] 删除字符使字符串变好
#

# @lc code=start
class Solution:
    # 同向双指针
    def makeFancyString(self, s: str) -> str:
        ans = []
        n = len(s)
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[start]:
                i += 1
            ans.append(s[start] * (2 if i - start > 2 else i - start))
        return "".join(ans)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.makeFancyString("leeeeeeetcode")
    print(ans)
