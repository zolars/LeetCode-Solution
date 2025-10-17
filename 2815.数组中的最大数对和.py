#
# @lc app=leetcode.cn id=2815 lang=python3
#
# [2815] 数组中的最大数对和
#


# @lc code=start
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        ans = -1
        stock = [-1] * 10
        for num in nums:
            # max_num = max(
            #     num // 10000,
            #     num // 1000 - num // 10000 * 10,
            #     num // 100 - num // 1000 * 10,
            #     num // 10 - num // 100 * 10,
            #     num % 10,
            # )
            max_num = int(max(str(num)))
            if stock[max_num] == -1:
                stock[max_num] = num
            else:
                ans = max(ans, stock[max_num] + num)
                if num > stock[max_num]:
                    stock[max_num] = num

        return ans


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxSum(
        [
            3361,
            3880,
            2792,
            3391,
            491,
            4299,
            5535,
            7670,
            827,
            85,
            4937,
            10000,
            5416,
            2248,
            1616,
            7136,
            3728,
            5176,
            7753,
            866,
            3729,
            6175,
            7009,
            3232,
            6716,
            9068,
            3283,
            3399,
            7893,
            4692,
            2147,
            5222,
            6476,
            4520,
            6021,
        ]
    )
    print(ans)
