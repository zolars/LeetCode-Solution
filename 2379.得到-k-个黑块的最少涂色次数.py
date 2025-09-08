#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current = 0
        for block in blocks[:k]:
            if block == "W":
                current += 1
        ans = current
        left = 0
        for block in blocks[k:]:
            if block == "W":
                current += 1
            if blocks[left] == "W":
                current -= 1
            ans = max(current, ans)
            if ans == 0:
                return ans
            left += 1
        return ans


# @lc code=end
