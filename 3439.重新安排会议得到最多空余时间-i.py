#
# @lc app=leetcode.cn id=3439 lang=python3
#
# [3439] 重新安排会议得到最多空余时间 I
#

# @lc code=start
class Solution:
    def maxFreeTime(
        self,
        eventTime: int,
        k: int,
        startTime: list[int],
        endTime: list[int],
    ) -> int:
        emptys = []
        startTime = startTime + [eventTime]
        endTime = [0] + endTime
        n = len(startTime)
        i = 0
        while i < n:
            emptys.append(startTime[i] - endTime[i])
            i += 1
        # print(emptys, sum(emptys[0 : k + 1]))
        ans = current = sum(emptys[0 : k + 1])
        for i, value in enumerate(emptys[k + 1 :]):
            # print(ans, emptys[i], value)
            current += value - emptys[i]
            ans = max(ans, current)
        return ans


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxFreeTime(
        21,
        1,
        [7, 10, 16],
        [10, 14, 18],
    )
    print(ans)
