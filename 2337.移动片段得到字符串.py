#
# @lc app=leetcode.cn id=2337 lang=python3
#
# [2337] 移动片段得到字符串
#

# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(target)
        i, j = 0, 0
        while i < n and j < n:
            if target[i] == "_":
                i += 1
            elif target[i] == "L":
                while j < n:
                    if start[j] == "R":
                        return False
                    elif start[j] == "_":
                        j += 1
                    elif j < i:
                        return False
                    else:
                        i += 1
                        j += 1
                        break
            else:
                while j < n:
                    if j > i or start[j] == "L":
                        return False
                    elif start[j] == "_":
                        j += 1
                    elif start[j] == "R":
                        i += 1
                        j += 1
                        break
        if i == n and j < n:
            for c in start[j:]:
                if c != "_":
                    return False
        if j == n and i < n:
            for c in target[i:]:
                if c != "_":
                    return False
        return True


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.canChange(
        "R__",
        "_RR",
    )
    print(ans)
