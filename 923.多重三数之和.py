#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 多重三数之和
#

# @lc code=start
class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        from collections import Counter

        ans = 0
        arr.sort()
        cntArr = Counter(arr)
        for left, num in enumerate(arr[: len(arr) - 2]):
            cntArr[num] -= 1
            i, j, k = left + 1, len(arr) - 1, target - num
            if arr[i] + arr[i + 1] > k:
                break
            if arr[j] + arr[j - 1] < k:
                continue
            while i < j:
                current = arr[i] + arr[j]
                if current < k:
                    i += 1
                elif current > k:
                    j -= 1
                else:
                    if arr[i] == arr[j]:
                        ans += cntArr[arr[i]] * (cntArr[arr[i]] - 1) // 2
                    else:
                        ans += cntArr[arr[i]] * cntArr[arr[j]]
                    while i < j and arr[i] == arr[i + 1]:
                        i += 1
                    while i < j and arr[j] == arr[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
        return ans % (10**9 + 7)


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.threeSumMulti(
        arr=[1, 1, 2, 2, 2, 2],
        target=5,
    )
    print(ans)
