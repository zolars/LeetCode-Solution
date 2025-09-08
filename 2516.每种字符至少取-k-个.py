#
# @lc app=leetcode.cn id=2516 lang=python3
#
# [2516] 每种字符至少取 K 个
#

# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        stock = {"a": 0, "b": 0, "c": 0}
        ns = {"a": 0, "b": 0, "c": 0}
        for c in s:
            stock[c] += 1
        for c in stock:
            if stock[c] < k:
                return -1
            else:
                stock[c] -= k
        if len(s) == k * 3:
            return len(s)
        ans = 0
        left = 0
        for right, c in enumerate(s):
            ns[c] += 1
            while (
                ns["a"] > stock["a"]
                or ns["b"] > stock["b"]
                or ns["c"] > stock["c"]
                and left < right
            ):
                ns[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return len(s) - ans


# @lc code=end
