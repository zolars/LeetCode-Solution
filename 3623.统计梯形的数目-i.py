#
# @lc app=leetcode.cn id=3623 lang=python3
#
# [3623] 统计梯形的数目 I
#

# @lc code=start
class Solution:
    # TODO: 莫名其妙的过了
    def countTrapezoids(self, points: list[list[int]]) -> int:
        ans = 0
        stock = {}
        for point in points:
            if point[1] in stock:
                stock[point[1]] += 1
            else:
                stock[point[1]] = 1
        stock = [v * (v - 1) // 2 for v in stock.values() if v > 1]
        ans = s = 0
        for c in stock:
            ans += s * c
            s += c
        return ans % (10**9 + 7)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.countTrapezoids(
        points=[[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]],
    )
    print(ans)
