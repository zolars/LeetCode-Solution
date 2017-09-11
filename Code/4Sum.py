# 4Sum


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def threeSum(nums, target):
            """
            threeSum
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            i, ans = 0, []
            for i in xrange(len(nums) - 2):
                if i != 0 and nums[i] == nums[i - 1]:
                    continue

                l, r = i + 1, len(nums) - 1

                while l < r:
                    s = nums[i] + nums[l] + nums[r] - target
                    if s > 0:
                        r -= 1
                    elif s < 0:
                        l += 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1
                i += 1
            return ans

        nums = sorted(nums)
        ans = []
        for num, i in enumerate(nums):
            temp = threeSum(nums[num + 1:], target - i)
            if temp:
                for j in temp:
                    if [i] + j not in ans:
                        ans.append([i] + j)

        return ans


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
