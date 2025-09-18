#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#

# @lc code=start
class Solution:
    # TODO: 完全不会做
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        ans = j
        i = 0
        while i == 0 or arr[i - 1] <= arr[i]:
            while j < n and arr[i] > arr[j]:
                j += 1
            ans = min(ans, j - i - 1)
            i += 1
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.findLengthOfShortestSubarray(
        [16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15],
    )
    print(ans)
