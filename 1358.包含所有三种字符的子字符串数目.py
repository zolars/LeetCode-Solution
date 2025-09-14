#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#

# @lc code=start
class Solution:
    # 大道至简
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        stock = {"a": 0, "b": 0, "c": 0}
        left = 0
        for right, c in enumerate(s):
            stock[c] += 1
            while (
                stock["a"] > 0 and stock["b"] > 0 and stock["c"] > 0 and left <= right
            ):
                stock[s[left]] -= 1
                left += 1
            ans += left
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numberOfSubstrings(
        "abcb",
    )
    print(ans)
