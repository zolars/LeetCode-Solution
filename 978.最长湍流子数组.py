#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        ans = i = 0
        while i < n:
            start = i
            i += 1
            if i < n and arr[i] == arr[i - 1]:
                continue
            while i < n and (
                i - start < 2 or (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0
            ):
                i += 1

            if (
                start > 0
                and start < n - 1
                and (arr[start] - arr[start - 1]) * (arr[start + 1] - arr[start]) < 0
            ):
                ans = max(ans, i - start + 1)
            else:
                ans = max(ans, i - start)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxTurbulenceSize([9, 9])
    print(ans)
