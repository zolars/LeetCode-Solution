#
# @lc app=leetcode.cn id=2105 lang=python3
#
# [2105] 给植物浇水 II
#

# @lc code=start
class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        l, r = 0, len(plants) - 1
        currentA, currentB = capacityA, capacityB
        while l < r:
            if currentA < plants[l]:
                ans += 1
                currentA = capacityA
            currentA -= plants[l]

            if currentB < plants[r]:
                ans += 1
                currentB = capacityB
            currentB -= plants[r]
            l += 1
            r -= 1
        if l == r and max(currentA, currentB) < plants[l]:
            ans += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.minimumRefill(
        plants=[5],
        capacityA=10,
        capacityB=8,
    )
    print(ans)
