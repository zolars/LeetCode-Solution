# Two Sum


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return([lookup[target - num], i])
                break
            lookup[num] = i
        return([])

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        k = 0
        for i in nums:
            k += 1
            if target - i in nums[k:]:
                return(k - 1, nums[k:].index(target - i) + k)


if __name__ == '__main__':
    print(Solution().twoSum([1, 2, 3, 4], 6))
