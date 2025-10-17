#
# @lc app=leetcode.cn id=2001 lang=python3
#
# [2001] 可互换矩形的组数
#

from collections import defaultdict


# @lc code=start
class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        ans = 0
        stock = defaultdict(int)
        for rectangle in rectangles:
            t = rectangle[0] / rectangle[1]
            ans += stock[t]
            stock[t] += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.interchangeableRectangles(
        rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]],
    )
    print(ans)
