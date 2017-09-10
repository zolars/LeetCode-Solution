# 3Sum Closest


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)

        min = 10000
        for i in xrange(len(nums) - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = (nums[i] + nums[l] + nums[r]) - target
                if s == 0:
                    return target

                elif s > 0:
                    s = abs(s)
                    if s < min:
                        min = s
                        ans = nums[i] + nums[l] + nums[r]
                    r -= 1

                elif s < 0:
                    s = abs(s)
                    if s < min:
                        min = s
                        ans = nums[i] + nums[l] + nums[r]

                    l += 1

        return ans


if __name__ == '__main__':
    print(Solution().threeSumClosest([-12, 0, 12, 13, 14, 15], 12))
