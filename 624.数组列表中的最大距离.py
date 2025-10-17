#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624] 数组列表中的最大距离
#

# @lc code=start
class Solution:
    # TODO: 稍微有点点难，想清楚再写
    def maxDistance(self, arrays: list[list[int]]) -> int:
        stock = [(array[0], array[-1]) for array in arrays]
        min1 = 10001
        min2 = 10001
        max1 = -10001
        max2 = -10001
        for array in arrays:
            if array[0] < min1:
                min2 = min1
                min1 = array[0]
            elif array[0] < min2:
                min2 = array[0]
            if array[-1] > max1:
                max2 = max1
                max1 = array[-1]
            elif array[-1] > max2:
                max2 = array[-1]
        if (min1, max1) not in stock:
            return max1 - min1
        else:
            return max(max2 - min1, max1 - min2)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxDistance(
        [[-5, -2, 0, 1, 1, 2], [-7, -6, -3], [-8, -7, -4, -4, 0, 2, 3, 4]]
    )
    print(ans)
