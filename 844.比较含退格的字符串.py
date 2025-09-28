#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    # TODO: 先做个O(m+n)保过
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s = []
        for c in s:
            if c == "#":
                if result_s:
                    result_s.pop()
            else:
                result_s.append(c)
        result_t = []
        for c in t:
            if c == "#":
                if result_t:
                    result_t.pop()
            else:
                result_t.append(c)
        return result_s == result_t


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.backspaceCompare("y#fo##f", "y#f#o##f")
    print(ans)
