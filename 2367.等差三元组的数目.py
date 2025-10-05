#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 等差三元组的数目
#

# @lc code=start
class Solution:
    def arithmeticTriplets(
        self,
        nums: list[int],
        diff: int,
    ) -> int:
        ans = 0
        n = len(nums)
        i, j, k = 0, 1, 2
        while i <= n - 3 and j <= n - 2 and k <= n - 1:
            if i == j:
                j += 1
            if j == k:
                k += 1
            if nums[j] - nums[i] == diff:
                if nums[k] - nums[j] == diff:
                    ans += 1
                    i += 1
                    j += 1
                    k += 1
                elif nums[k] - nums[j] < diff:
                    k += 1
                else:
                    j += 1
            elif nums[j] - nums[i] < diff:
                j += 1
            else:
                i += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.arithmeticTriplets(
        nums=[0, 1, 4, 6, 7, 10],
        diff=3,
    )
    print(ans)
