#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        last_del = ""
        while l < r:
            if s[l] == s[r]:
                last_del = s[l]
                l += 1
                r -= 1
            elif s[l] == last_del:
                l += 1
            elif s[r] == last_del:
                r -= 1
            else:
                return r - l + 1
        if s[l] == last_del:
            return 0
        else:
            return 1


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.minimumLength("abbbbbbbbbbbbbbbbbbba")
    print(ans)
