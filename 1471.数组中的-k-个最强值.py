#
# @lc app=leetcode.cn id=1471 lang=python3
#
# [1471] 数组中的 k 个最强值
#

# @lc code=start
class Solution:
    # 双指针
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        ans = []
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        i, j = 0, n - 1
        while i <= j and len(ans) < k:
            if abs(arr[i] - m) > abs(arr[j] - m) or (
                abs(arr[i] - m) == abs(arr[j] - m) and arr[i] > arr[j]
            ):
                ans.append(arr[i])
                i += 1
            else:
                ans.append(arr[j])
                j -= 1
        return ans

    # TODO: 定长滑动窗口法实现


# @lc code=end
