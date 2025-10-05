#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        prev_count = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[start]:
                i += 1
            ans += min(prev_count, i - start)
            prev_count = i - start
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.countBinarySubstrings("00110011")
    print(ans)
