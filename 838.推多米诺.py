#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = list("L" + dominoes + "R")  # 前后各加一个哨兵
        i = 0
        n = len(s)
        while i < n - 1:
            start = i
            i += 1
            while i < n - 1 and s[i] == ".":
                i += 1
            if s[start] == s[i]:
                s[start:i] = [s[start]] * (i - start)
            elif s[start] == "R" and s[i] == "L":
                half_length = (i - start - 1) // 2
                s[start + 1 : start + half_length + 1] = ["R"] * half_length
                s[i - half_length : i] = ["L"] * half_length
        return "".join(s[1:-1])


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.pushDominoes(".L.R...LR..L..")
    print(ans)
