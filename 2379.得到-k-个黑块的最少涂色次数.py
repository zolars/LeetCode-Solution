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
        result = current
        left = 0
        for block in blocks[k:]:
            if block == "W":
                current += 1
            if blocks[left] == "W":
                current -= 1
            result = max(current, result)
            if result == 0:
                return result
            left += 1
        return result


# @lc code=end
