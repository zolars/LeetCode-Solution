#
# @lc app=leetcode.cn id=2024 lang=python3
#
# [2024] 考试的最大困扰度
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        len_change_T = 0
        left_T = 0
        len_change_F = 0
        left_F = 0
        for right, answer in enumerate(answerKey):
            if answer == "T":
                len_change_T += 1
                while len_change_T > k:
                    if answerKey[left_T] == "T":
                        len_change_T -= 1
                    left_T += 1
            else:
                len_change_F += 1
                while len_change_F > k:
                    if answerKey[left_F] == "F":
                        len_change_F -= 1
                    left_F += 1
            ans = max(ans, right - left_T + 1)
            ans = max(ans, right - left_F + 1)

        return ans


# @lc code=end
