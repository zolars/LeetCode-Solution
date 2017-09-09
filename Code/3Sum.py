class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        i, ans = 0, []

        for i in xrange(len(nums) - 2):
            if nums[i] > 0 or (i != 0 and nums[i] == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1

            print i, l, r

            while l < r:
                s = nums[i] + nums[l] + nums[r]
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


if __name__ == '__main__':
    print(Solution().threeSum([-1, -1, 0, 1]))
