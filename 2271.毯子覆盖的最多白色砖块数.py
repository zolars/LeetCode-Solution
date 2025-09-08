#
# @lc app=leetcode.cn id=2271 lang=python3
#
# [2271] 毯子覆盖的最多白色砖块数
#

# @lc code=start
class Solution:
    # 不能从左端点对齐，得对齐右端点
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda item: item[0])
        ans, covered, left = 0, 0, 0
        for x, y in tiles:
            # if y - x + 1 >= carpetLen:
            #     return carpetLen
            covered += y - x + 1
            while tiles[left][1] <= y - carpetLen:
                covered -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # key
            w = max((y - carpetLen) - tiles[left][0] + 1, 0)
            ans = max(ans, covered - w)
        return ans


# @lc code=end

if __name__ == "__main__":
    testcase = [[1, 11], [20, 150]], 20
    solution = Solution()
    res = solution.maximumWhiteTiles(*testcase)
    print(res)
