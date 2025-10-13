#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: list[int]) -> int:
        ans = []
        n = len(ratings)
        i = 0
        while i < n:
            start = i
            ans.append(1)
            i += 1
            while i < n and ratings[i] > ratings[i - 1]:
                ans.append(ans[-1] + 1)
                i += 1
        i = n - 1
        while i >= 0:
            start = i
            ans[start] = max(ans[start], 0)
            i -= 1
            while i >= 0 and ratings[i] > ratings[i + 1]:
                ans[i] = max(ans[i], ans[i + 1] + 1)
                i -= 1
        return sum(ans)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.candy([1, 0, 2])
    print(ans)
