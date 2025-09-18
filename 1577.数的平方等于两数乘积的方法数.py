#
# @lc app=leetcode.cn id=1577 lang=python3
#
# [1577] 数的平方等于两数乘积的方法数
#

# @lc code=start
class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        def twoMultiple(arr, k):
            res = 0
            i, j = 0, len(arr) - 1
            while i < j:
                current = arr[i] * arr[j]
                if current < k:
                    i += 1
                elif current > k:
                    j -= 1
                else:
                    ii = i
                    while ii < j and arr[ii] == arr[ii + 1]:
                        ii += 1
                    jj = j
                    while i < jj and arr[jj] == arr[jj - 1]:
                        jj -= 1
                    if arr[i] != arr[j]:
                        res += (j - jj + 1) * (ii - i + 1)
                    else:
                        res += (j - i + 1) * (j - i) // 2
                    i = ii + 1
                    j = jj - 1
            return res

        ans = 0
        nums1.sort()
        nums2.sort()
        for num in nums1:
            ans += twoMultiple(nums2, num**2)
        for num in nums2:
            ans += twoMultiple(nums1, num**2)
        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.numTriplets(
        [1, 1],
        [1, 1, 1],
    )
    print(ans)
