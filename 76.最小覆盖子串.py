#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        ans_length = len(s)
        stock = {}
        for c in t:
            if c in stock:
                stock[c] += 1
            else:
                stock[c] = 1
        current = {}
        left = 0
        for right, c in enumerate(s):
            if c in current:
                current[c] += 1
            else:
                current[c] = 1
            if c in stock and current[c] >= stock[c]:
                flag = True
                for key, value in stock.items():
                    if key not in current or current[key] < value:
                        flag = False
                while flag and left <= right:
                    if right - left + 1 <= ans_length:
                        ans_length = right - left + 1
                        ans = s[left : right + 1]
                        if ans_length == len(t):
                            return ans
                    current[s[left]] -= 1
                    if s[left] in stock and current[s[left]] < stock[s[left]]:
                        left += 1
                        break
                    else:
                        left += 1
                        continue
        return ans


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    ans = sol.minWindow(
        "a",
        "aa",
    )
    print(ans)
