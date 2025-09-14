#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution:
    # 返回最靠近 x 的 k 个数
    def findClosestElements(
        self,
        arr: list[int],
        k: int,
        x: int,
    ) -> list[int]:
        i, j = 0, len(arr) - 1
        while j - i + 1 > k:
            a, b = arr[i], arr[j]
            if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
                j -= 1
            else:
                i += 1
        return arr[i : j + 1]


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findClosestElements(
        arr=[1, 1, 2, 3, 4, 5],
        k=4,
        x=-1,
    )
    print(ans)
